# apps/auth/views/registration.py

from rest_framework import (
    permissions, status
)
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from apps.auth.serializers import RegistrationSerializer


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def registration_confirm(request) -> Response:
    """
    Registers user (accepts, third party, therefore password is not required)
    anyone can call this.
    """
    # Bind request data to the serializer
    serializer = RegistrationSerializer(data=request.data)
    # Validata, or throw a 400 with detailed error
    serializer.is_valid(raise_exception=True)
    # Perform the create() logic and get back the new user
    serializer.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)
