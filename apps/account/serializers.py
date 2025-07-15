# serializers.py

from django.core.exceptions import ValidationError as DjangoValidationError
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from .models import CustomUser, CustomUserProfile


# PROFILE SERIALIZER (read-only)
class CustomUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserProfile
        fields = (
            'phone',
            'is_phone_verified',
            'created_at',
            'updated_at',
        )
        read_only_fields = ('created_at', 'updated_at')


# USER READ SERIALIZER (read-only)
class CustomUserReadSerializer(serializers.ModelSerializer):
    profile = CustomUserProfile()

    class Meta:
        model = CustomUser
        fields = (
            'id',
            'email',
            'is_staff',
            'is_active',
        )
        read_only_fields = ('id',)


# USER REGISTRATION SERIALIZER (signup + optional password)
class CustomUserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=False,
        allow_null=True,
        allow_blank=True
    )
    confirm_password = serializers.CharField(
        write_only=True,
        required=False,
        allow_null=True,
        allow_blank=True
    )

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'password', 'confirm_password')
        read_only_fields = ('id',)
        extra_kwargs = {
            'email': {'required': True}
        }

    def _handle_password(self, user, password, confirm_password):
        # If a password is provided, ensure it matches and validate strength
        if password:
            if password != confirm_password:
                raise serializers.ValidationError({
                    'confirm_password': 'Passwords do not match.'
                })
            try:
                validate_password(password)
            except DjangoValidationError as e:
                raise serializers.ValidationError({'password': e.messages})
            user.set_password(password)
        else:
            # No password means third-party auth;
            # make unusable to prevent login by password
            user.set_unusable_password()

    def validate_email(self, value):
        if CustomUser.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError(
                'A user with that email already exists.'
            )
        return value

    def create(self, validated_data):
        # Extract and remove confirm_password from the data
        confirm_password = validated_data.pop('confirm_password', '')
        password = validated_data.pop('password', '')

        # Instantiate user without saving
        user = CustomUser(
            email=validated_data['email'],
            is_active=False,
        )
        user.save()

        # Handle password (or mark unusable)
        self._handle_password(user, password, confirm_password)
        user.save()
        return user
