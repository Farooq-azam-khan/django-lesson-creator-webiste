from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import UserProfileModel

class UserDetailView(DetailView):
    model = UserProfileModel
