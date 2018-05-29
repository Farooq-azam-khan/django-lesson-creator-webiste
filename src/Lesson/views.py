from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.db.models import Q
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView
from django.http import HttpResponse, HttpResponseRedirect

from .models import LessonPlan
from .forms import LessonCreateForm, LessonPlanCreateForm

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





    # def get_object(self, *args, **kwargs):
    #     lsn_id = self.kwargs.get('lsn_id')
    #     print("lsn_id:", lsn_id)
    #     obj = get_object_or_404(LessonPlan, id=lsn_id)
    #     print("obj:",obj)
    #     return obj

class CreateLessonFormView(FormView):
    template_name = "form.html"
    form_class = LessonCreateForm
    success_url = '/lessons/'

    def form_valid(self, form):
        print("valid form")
        return super().form_valid(form)


def create_lesson_create_view(request):
    form = LessonPlanCreateForm(request.POST or None)
    errors = None
    context = {'errors':errors, 'form':form}

    template_name = 'form.html'
    if form.is_valid():
        print("valid form")
        form.save()
        return HttpResponseRedirect("/lessons/")
    if form.errors:
        errors = form.errors
    return render(request, template_name, context)


class LessonPlanCreateView(CreateView):
    form_class = LessonPlanCreateForm
    template_name = "form.html"
    success_url = '/lessons/'
