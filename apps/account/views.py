# apps/account/views.py

from typing import Any

from rest_framework import generics, permissions

from .serializers import UserReadSerializer


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserReadSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self) -> Any:
        """
        Return the current authenticated user
        """
        return self.request.user
