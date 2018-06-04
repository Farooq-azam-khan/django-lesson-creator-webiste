from django.db import models
from django.db.models.signals import pre_save, post_save
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
from .utils import unique_slug_generator
from .validators import validate_subject

User = settings.AUTH_USER_MODEL
def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

class LessonPlan(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user))
    lesson_name = models.CharField(max_length=50, unique=True) #TODO:make is unique for user
    subtitle = models.CharField(max_length=100, unique=False, blank=True, null=True)
    abstract = models.CharField(max_length=200, blank=True, null=True)
    is_draft = models.BooleanField(default=False)
    subject = models.CharField(max_length=100, validators=[validate_subject])
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.lesson_name

    def get_absolute_url(self):
        return reverse('Lesson:detail', kwargs={'slug':self.slug})


    @property
    def title(self):
        return self.lesson_name

    class Meta:
        ordering = ['-updated', '-timestamp']

class ChapterModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user), default=1)
    chapter_title = models.CharField(max_length=120, unique=True)
    chapter_quote = models.CharField(max_length=200, blank=True, null=True)
    chapter_quote_author = models.CharField(max_length=100, blank=True, null=True)
    chapter_introduction = models.TextField(help_text="Write your Introduction here.")
    lesson = models.ForeignKey(LessonPlan, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-timestamp']

    # def get_chapter_introduction(self):
    #     return self.chapter_introduction
    # def get_chapter_quote(self):
    #     return self.chapter_quote

    def get_absolute_url(self):
        return reverse('Lesson:detail-chapter', kwargs={'pk':self.pk})

    def __str__(self):
        return self.chapter_title

class SectionModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user), default=1)
    section_title = models.CharField(max_length=120, unique=False)
    section_content = models.TextField(help_text="Write your content here.")
    chapter = models.ForeignKey(ChapterModel, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('Lesson:detail-section', kwargs={'pk':self.pk})

    def __str__(self):
        return self.section_title

def pre_save_receiver(sender, instance, *args, **kwargs):
    # print(instance.timestamp)
    instance.subject = instance.subject.capitalize()
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_receiver, sender=LessonPlan)
