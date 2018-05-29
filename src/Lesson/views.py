from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.db.models import Q
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import LessonPlan
from .forms import LessonPlanCreateForm

class LessonListView(LoginRequiredMixin, ListView):
    model = LessonPlan
    queryset = LessonPlan.objects.all()

class SearchLessonsListView(LoginRequiredMixin, ListView):
    model = LessonPlan
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = LessonPlan.objects.filter(
                                            Q(subject__iexact=slug)|
                                            Q(subject__icontains=slug)|
                                            Q(lesson_name__iexact=slug)|
                                            Q(lesson_name__icontains=slug))
        else:
            queryset = LessonPlan.objects.none()
        return queryset

class LessonPlanDetailView(LoginRequiredMixin, DetailView):
    model = LessonPlan

class LessonPlanCreateView(LoginRequiredMixin, CreateView):
    form_class = LessonPlanCreateForm
    template_name = "form.html"
    success_url = '/lessons/'
    login_url = '/login/'
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(LessonPlanCreateView, self).form_valid(form)
