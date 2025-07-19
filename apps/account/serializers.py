# serializers.py
from rest_framework import serializers

from .models import CustomUser, CustomUserProfile


# PROFILE SERIALIZER (read-only for fetch)
class ProfileReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserProfile
        fields = (
            'phone',
            'is_phone_verified',
            'created_at',
            'updated_at',
        )
        read_only_fields = (
            'phone',
            'is_phone_verified',
            'created_at',
            'updated_at'
        )


# USER READ SERIALIZER (read-only for fetch)
class UserReadSerializer(serializers.ModelSerializer):
    # nest the serializer
    profile = ProfileReadSerializer(read_only=True)

    class Meta:
        model = CustomUser
        fields = (
            'id',
            'email',
            'is_staff',
            'is_active',
            'profile',           # ← add this
        )
        read_only_fields = (
            'id',
            'email',
            'is_staff',
            'is_active',
            'profile'
        )
