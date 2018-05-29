from django import forms

from .models import LessonPlan

class LessonCreateForm(forms.Form):
    lesson_name = forms.CharField(required=True)
    subtitle = forms.CharField(required=False)
    content = forms.CharField(widget=forms.Textarea, required=True)
    is_draft = forms.BooleanField(required=False)
    subject = forms.CharField(required=True)

    def clean_lesson_name(self):
        lesson_name = self.cleaned_data.get("lesson_name")
        if lesson_name == 'hello':
            raise forms.ValidationError("error: not a valid title")
        return lesson_name

class LessonPlanCreateForm(forms.ModelForm):
    class Meta:
        model = LessonPlan
        fields = [
            'lesson_name',
            'subtitle',
            'content',
            'is_draft',
            'subject'
        ]
