from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import (
    Post,
)


@receiver(post_save, sender=Post)
def add_score(instance, **kwargs):
    obj = instance.user_profile
    obj.score += 1
    obj.save()
