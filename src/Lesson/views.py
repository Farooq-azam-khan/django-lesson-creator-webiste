from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.db.models import Q
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView
from django.http import HttpResponse, HttpResponseRedirect

from .models import LessonPlan
from .forms import LessonPlanCreateForm

class LessonListView(ListView):
    model = LessonPlan
    queryset = LessonPlan.objects.all()

class SearchLessonsListView(ListView):
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

class LessonPlanDetailView(DetailView):
    model = LessonPlan

class LessonPlanCreateView(CreateView):
    form_class = LessonPlanCreateForm
    template_name = "form.html"
    success_url = '/lessons/'
