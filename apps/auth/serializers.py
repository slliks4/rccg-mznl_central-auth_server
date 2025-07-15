# apps/account/serializers.py

from django.core.exceptions import ValidationError as DjangoValidationError
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from apps.account.models import CustomUser


# Registration Serializer
class RegistrationSerializer(serializers.ModelSerializer):
    # Allows 3rd party auth
    password = serializers.CharField(
        write_only=True, required=False, allow_null=True, allow_blank=True
    )
    confirm_password = serializers.CharField(
        write_only=True, required=False, allow_null=True, allow_blank=True
    )

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'password', 'confirm_password')
        read_only_fields = ('id',)
        extra_kwargs = {'email': {'required': True}}

    # Validate password
    def validate(self, attrs):
        pw = attrs.get('password') or ''
        cpw = attrs.get('confirm_password') or ''

        # Only validate passwords if one was provided
        if pw:
            if pw != cpw:
                raise serializers.ValidationError({
                    'confirm_password': 'Passwords do not match.'
                })
            try:
                validate_password(pw)
            except DjangoValidationError as e:
                raise serializers.ValidationError({'password': e.messages})

        return attrs

    def create(self, validated_data):
        # Pull out password fields
        pw = validated_data.pop('password', '')
        _ = validated_data.pop('confirm_password', '')

        # Instantiate (but don't hit unique constraints twice)
        user = CustomUser(email=validated_data['email'], is_active=False)
        user.save()

        # Handle password or mark unusable
        if pw:
            user.set_password(pw)
        else:
            user.set_unusable_password()

        user.save()
        return user
