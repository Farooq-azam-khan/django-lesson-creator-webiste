from django.db import models

# Create your models here.
class LessonPlan(models.Model):
    lesson_name = models.CharField(max_length=30, unique=True)
    content = models.TextField()
    subject = models.CharField(max_length=100, default="physics")
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.lesson_name
