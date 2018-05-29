from django.db import models
from django.db.models.signals import pre_save, post_save

from .utils import unique_slug_generator

# Create your models here.
class LessonPlan(models.Model):
    lesson_name = models.CharField(max_length=100, unique=True)
    subtitle = models.CharField(max_length=200, unique=False, blank=True, null=True)
    content = models.TextField()
    is_draft = models.BooleanField(default=True)
    subject = models.CharField(max_length=100, default="physics")
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.lesson_name

    @property
    def title(self):
        return self.lesson_name

    class Meta:
        pass

def pre_save_receiver(sender, instance, *args, **kwargs):
    # print('saving...')
    print(instance.timestamp)
    # if slug doesnt exist for that instance/obj
    if not instance.slug:
        # create it/
        # dont need to call save
        instance.slug = unique_slug_generator(instance)

# def post_save_receiver(sender, instance, created, *args, **kwargs):
#     print("saved")
#     print(instance.timestamp)

pre_save.connect(pre_save_receiver, sender=LessonPlan)
# post_save.connect()
