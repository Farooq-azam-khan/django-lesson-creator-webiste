from django.urls import path
from django.conf.urls import url

from Profile.views import UserDetailView

app_name="Profile"

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', UserDetailView.as_view(), name="user-detailview"),
]
