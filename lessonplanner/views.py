from django.utils import timezone
from .models import Lesson
from django.shortcuts import render, get_object_or_404

# Create your views here.

def lesson_list(request):
    lessons = Lesson.objects.order_by('unit')
    return render(request, 'lessonplanner/lesson_list.html', {'Lessons': lessons })

def lesson_detail(request, pk):
    lessons = get_object_or_404(Lesson, pk=pk)
    return render(request, 'lessonplanner/lesson_detail.html', {'Lessons': lessons })
