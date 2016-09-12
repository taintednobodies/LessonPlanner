from django.shortcuts import render
from django.utils import timezone
from .models import Lesson

# Create your views here.

def lesson_list(request):
    lessons = Lesson.objects.order_by('date')
    return render(request, 'lessonplanner/lesson_list.html', {'Lessons': lessons})
