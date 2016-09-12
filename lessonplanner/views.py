from django.utils import timezone
from .models import Lesson
from django.shortcuts import render, get_object_or_404
from .forms import LessonForm
from django.shortcuts import redirect

# Create your views here.

def lesson_list(request):
    lessons = Lesson.objects.order_by('unit')
    return render(request, 'lessonplanner/lesson_list.html', {'Lessons': lessons })

def lesson_detail(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    return render(request, 'lessonplanner/lesson_detail.html', {'Lesson': lesson })
'''
def lesson_new(request):
    form = LessonForm()
    return render(request, 'lessonplanner/lesson_edit.html', {'form': form})
'''
def lesson_new(request):
    if request.method == "POST":
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.author = request.user
            lesson.save()
            return redirect('lesson_detail', pk=lesson.pk)
    else:
        form = LessonForm()
    return render(request, 'lessonplanner/lesson_edit.html', {'form': form})

def lesson_search(request, search):
    lessons = Lesson.objects.filter(summary__search)
    return render(request, "lessonplanner/lesson_search.html", {'Lessons' : lessons })
