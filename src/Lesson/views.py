from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.db.models import Q
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


class SearchLessonsListView(ListView):
    model = LessonPlan
    template_name = "Lesson/lesson.html"

    def get_queryset(self):
        #kwargs gets a dictionary
        print(self.kwargs)
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
