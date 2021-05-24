from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from app1.models import Profile

@receiver(post_save, sender=User)
def save_Profile(sender, instance, created, **kwarg):
    if created:
        Profile.objects.create(user=instance, name=instance.username)



