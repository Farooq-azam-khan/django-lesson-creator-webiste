from django import forms

class LessonCreateForm(forms.Form):
    lesson_name = forms.CharField(required=True)
    subtitle = forms.CharField(required=False)
    content = forms.CharField(widget=forms.Textarea, required=True)
    is_draft = forms.BooleanField(required=False)
    subject = forms.CharField(required=True)
