"""LessonMaker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path
from django.conf.urls import url
# from Lesson.views import lesson_listview
from Lesson.views import (LessonListView,
                        SearchLessonsListView,
                        LessonPlanDetailView,
                        LessonPlanCreateView)
from Profile.views import UserDetailView

from Finance.views import FinanceDetailView
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name="home"),
    url(r'^finance/(?P<pk>[\w-]+)/$', FinanceDetailView.as_view(), name="finance"),
    url(r'^profile/(?P<slug>[\w-]+)/$', UserDetailView.as_view(), name="user-detailview"),
    url(r'^lessons/$', LessonListView.as_view(), name="lessons-list"),
    url(r'^lessons/create/$', LessonPlanCreateView.as_view(), name="create-lesson"),
    url(r'^lessons/(?P<slug>[\w-]+)/$', LessonPlanDetailView.as_view(), name="search-lesson"),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name="about"),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name="contact"),
    url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
