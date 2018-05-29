from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save, post_save


from .utils import unique_slug_generator

User = settings.AUTH_USER_MODEL
def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

# Create your models here.
class UserProfileModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user))
    # profile_image = models.ImageField(null=True, blank=True, upload_to="")
    slug = models.SlugField(unique=True, null=True, blank=True)

    @property
    def title(self):
        return self.owner.username

    def __str__(self):
        return self.owner.username



def pre_save_receiver(sender, instance, *args, **kwargs):
    instance.owner.username = instance.owner.username.capitalize()
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_receiver, sender=UserProfileModel)
