from django.urls import path
from django.conf.urls import url
from Lesson.views import (LessonListView,
                        SearchLessonsListView,
                        LessonPlanDetailView,
                        LessonPlanCreateView,
                        LessonPlanUpdateview,
                        ChapterCreateView,
                        ChapterListView,
                        ChapterDetailView,
                        ChapterUpdateView,
                        SectionCreateView,
                        SectionUpdateView,
                        SectionDetailView,
                        SectionListView,
                        )
app_name="Lesson"

urlpatterns = [
    url(r'^create/$', LessonPlanCreateView.as_view(), name="create"),
    url(r'^chapters/$', ChapterListView.as_view(), name="list-chapters"),
    url(r'^chapters/create/$', ChapterCreateView.as_view(), name="create-chapter")
    ,
    url(r'^chapters/sections/$', SectionListView.as_view(), name="list-sections"),
    url(r'^chapters/sections/create/$', SectionCreateView.as_view(), name="create-section"),
    url(r'^chapters/sections/(?P<pk>\d+)/$', SectionDetailView.as_view(), name="detail-section"),
    url(r'^chapters/sections/(?P<pk>\d+)/update/$', SectionUpdateView.as_view(), name="update-section"),

    url(r'^chapters/(?P<pk>\d+)/$', ChapterDetailView.as_view(), name="detail-chapter"),
    url(r'^chapters/(?P<pk>\d+)/update/$', ChapterUpdateView.as_view(), name="update-chapter"),
    url(r'^(?P<slug>[\w-]+)/$', LessonPlanDetailView.as_view(), name="detail"),
    url(r'^(?P<slug>[\w-]+)/chapters/$', ChapterListView.as_view(), name="list-chapters"),


    url(r'^(?P<slug>[\w-]+)/update/$', LessonPlanUpdateview.as_view(), name="update-lessonplan"),
    url(r'^$', LessonListView.as_view(), name="list"),
]
