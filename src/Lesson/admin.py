from django.contrib import admin

from .models import LessonPlan, ChapterModel, SectionModel
admin.site.register(LessonPlan)
admin.site.register(ChapterModel)
admin.site.register(SectionModel)
