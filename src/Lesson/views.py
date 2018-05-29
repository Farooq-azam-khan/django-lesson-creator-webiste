from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.db.models import Q
from django.views.generic.detail import DetailView

from .models import LessonPlan

class LessonListView(ListView):
    model = LessonPlan
    # paginate_by = 1
    # template_name = "Lesson/lesson.html"
    queryset = LessonPlan.objects.all()


class SearchLessonsListView(ListView):
    model = LessonPlan
    # template_name = "Lesson/lesson.html"

    def get_queryset(self):
        #kwargs gets a dictionary
        # print(self.kwargs)
        slug = self.kwargs.get("slug")
        # print(slug)
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

    def get_context_data(self, *args, **kwargs):
        context = super(LessonPlanDetailView, self).get_context_data(*args, **kwargs)
        # print(self.kwargs)
        # print(context)
        return context

    def get_object(self, *args, **kwargs):
        lsn_id = self.kwargs.get('lsn_id')
        print("lsn_id:", lsn_id)
        obj = get_object_or_404(LessonPlan, id=lsn_id)
        print("obj:",obj)
        return obj
