from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = settings.AUTH_USER_MODEL
def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

# Create your models here.
class UserProfileModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user))
    profile_image = models.ImageField(null=True, blank=True, upload_to="")

    def __str__(self):
        return self.owner.username
