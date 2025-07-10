# Imports
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import CustomUser, CustomUserProfile


# Signal to auto-create profile when a CustomUser is created
@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        CustomUserProfile.objects.create(user=instance)
