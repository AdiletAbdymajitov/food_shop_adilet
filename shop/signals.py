from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver

from shop.models import UserProfile


@receiver(post_save, sender=User)
def create_profile(instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
