from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import Finance

class FinanceDetailView(DetailView):
    model = Finance
