from django import forms

from .models import LessonPlan
from .validators import validate_subject

# class LessonCreateForm(forms.Form):
#     lesson_name = forms.CharField(required=True)
#     subtitle = forms.CharField(required=False)
#     content = forms.CharField(widget=forms.Textarea, required=True)
#     is_draft = forms.BooleanField(required=False)
#     subject = forms.CharField(required=True)
#
#     def clean_lesson_name(self):
#         lesson_name = self.cleaned_data.get("lesson_name")
#         if lesson_name == 'hello':
#             raise forms.ValidationError("error: not a valid title")
#         return lesson_name

class LessonPlanCreateForm(forms.ModelForm):
    # subject = forms.CharField(required=True, validators=[validate_subject])
    class Meta:
        model = LessonPlan
        fields = [
            'lesson_name',
            'subtitle',
            'content',
            'is_draft',
            'subject'
        ]

    def clean_lesson_name(self):
        lesson_name = self.cleaned_data.get("lesson_name")
        if lesson_name == 'chem-g11':
            raise forms.ValidationError("error: not a valid title")
        return lesson_name
    # def clean_subject(self):
    #     subject = self.cleaned_data.get('subject')
    #     if subject not in VALID_SUBJECTS:
    #         ret_raise = "Subjects must be one of the following: {}".format(VALID_SUBJECTS)
    #         raise forms.ValidationError(ret_raise)
    #     return subject

# VALID_SUBJECTS = ['Math', 'Physics', 'English',
# 'Computer Science', 'History']
