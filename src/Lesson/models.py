from django.db import models
from django.db.models.signals import pre_save, post_save

from .utils import unique_slug_generator
from .validators import validate_subject

class LessonPlan(models.Model):
    lesson_name = models.CharField(max_length=100, unique=True)
    subtitle = models.CharField(max_length=200, unique=False, blank=True, null=True)
    content = models.TextField()
    is_draft = models.BooleanField(default=False)
    subject = models.CharField(max_length=100, validators=[validate_subject])
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
    # print(instance.timestamp)
    instance.subject = instance.subject.capitalize()
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_receiver, sender=LessonPlan)
