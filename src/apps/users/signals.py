# ...existing code...
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from apps.core.tasks import generate_thumbnails

@receiver(post_save, sender=User)
def user_post_save(sender, instance, created, **kwargs):
    if instance.avatar:
        generate_thumbnails.delay('users.User', instance.pk, 'avatar')

