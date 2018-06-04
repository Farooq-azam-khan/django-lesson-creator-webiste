from django.urls import path
from django.conf.urls import url

from Finance.views import FinanceDetailView

app_name="Profile"

urlpatterns = [
    url(r'^(?P<pk>[\w-]+)/$', FinanceDetailView.as_view(), name="finance"),
]
