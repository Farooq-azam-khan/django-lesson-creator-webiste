from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.db.models import Q
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import LessonPlan, ChapterModel, SectionModel
from .forms import LessonPlanCreateForm, ChapterForm, SectionForm

class LessonListView(LoginRequiredMixin, ListView):
    model = LessonPlan

    def get_queryset(self):
        return LessonPlan.objects.filter(owner=self.request.user)


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
    def get_queryset(self):
        return LessonPlan.objects.filter(owner=self.request.user)

class LessonPlanCreateView(LoginRequiredMixin, CreateView):
    form_class = LessonPlanCreateForm
    template_name = "form.html"
    success_url = '/lessons/'
    login_url = '/login/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(LessonPlanCreateView, self).form_valid(form)

class LessonPlanUpdateview(LoginRequiredMixin, UpdateView):
    form_class = LessonPlanCreateForm
    template_name = "form.html"
    success_url = '/lessons/'
    login_url = 'login/'
    def get_queryset(self):
        queryset = LessonPlan.objects.filter(owner=self.request.user)
        return queryset

# Chapters
class ChapterListView(LoginRequiredMixin, ListView):
    model = ChapterModel

    def get_queryset(self):
        # TODO: filter by lesson
        print("filter: ", ChapterModel.objects.all())
        return ChapterModel.objects.filter(owner=self.request.user)

class ChapterCreateView(LoginRequiredMixin, CreateView):
    form_class = ChapterForm
    template_name = "form.html"
    success_url = "/lessons/" # + slug
    login_url = '/login'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user
        return super().form_valid(form)

class ChapterDetailView(LoginRequiredMixin, DetailView):
    model = ChapterModel
    def get_queryset(self, *args, **kwargs):
        print("kwargs:", kwargs)
        return ChapterModel.objects.filter(owner=self.request.user)

class ChapterUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ChapterForm
    template_name = "form.html"
    success_url = '/lessons/'
    login_url = 'login/'

    def get_queryset(self, *args, **kwargs):
        print("kwargs:", kwargs)
        return ChapterModel.objects.filter(owner=self.request.user)

# Section
class SectionCreateView(LoginRequiredMixin, CreateView):
    form_class = SectionForm
    template_name = "form.html"
    success_url = "/lessons/" # + slug
    login_url = '/login'

class SectionUpdateView(LoginRequiredMixin, UpdateView):
    form_class = SectionForm
    template_name = "form.html"
    success_url = '/lessons/'
    login_url = 'login/'

    def get_queryset(self, *args, **kwargs):
        print("kwargs:", kwargs)
        return SectionModel.objects.filter(owner=self.request.user)

class SectionDetailView(LoginRequiredMixin, DetailView):
    model = SectionModel
    def get_queryset(self, *args, **kwargs):
        print("kwargs:", kwargs)
        return SectionModel.objects.filter(owner=self.request.user)

class SectionListView(LoginRequiredMixin, ListView):
    model = SectionModel

    def get_queryset(self):
        # TODO: filter by chapter
        return SectionModel.objects.filter(owner=self.request.user)
