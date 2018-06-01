from django.urls import path
from django.conf.urls import url
from Lesson.views import (LessonListView,
                        SearchLessonsListView,
                        LessonPlanDetailView,
                        LessonPlanCreateView)

urlpatterns = [
    url(r'^$', LessonListView.as_view(), name="list"),
    url(r'^create/$', LessonPlanCreateView.as_view(), name="create"),
    url(r'^(?P<slug>[\w-]+)/$', LessonPlanDetailView.as_view(), name="detail"),
]
