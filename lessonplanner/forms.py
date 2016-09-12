from django import forms
from .models import Lesson

class LessonForm (forms.ModelForm):
    class Meta:
            model = Lesson
            fields = ('className', 'unit', 'chapter', 'summary', 'materials', 'description',)
