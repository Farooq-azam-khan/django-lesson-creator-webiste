from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView

from .models import UserProfileModel

class UserDetailView(DetailView):
    model = UserProfileModel


# class UserHomeView(TemplateView):
#     template_name = 'home.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['user'] = UserProfileModel.objects.get(owner=self.request.user)
#         print(context)
#         return context
