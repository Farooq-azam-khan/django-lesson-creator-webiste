from django.contrib import admin

from .models import LessonPlan, Chapter, Section
admin.site.register(LessonPlan)
admin.site.register(Chapter)
admin.site.register(Section)
