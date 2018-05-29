from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from .models import LessonPlan
# def lesson_listview(request):
#     template_name = 'Lesson/lesson.html'
#     queryset = LessonPlan.objects.all()
#     context = {
#     "obj_list": queryset
#     }
#     return render(request, template_name, context)

class LessonListView(ListView):
    model = LessonPlan
    # paginate_by = 1
    template_name = "Lesson/lesson.html"
    queryset = LessonPlan.objects.all()


class EnglishLessonsListView(ListView):
    model = LessonPlan
    # paginate_by = 1
    template_name = "Lesson/lesson.html"
    queryset = LessonPlan.objects.filter(subject__iexact="english")
