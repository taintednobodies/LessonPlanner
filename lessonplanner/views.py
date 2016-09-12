from django.shortcuts import render

# Create your views here.

def lesson_list(request):
    return render(request, 'lessonplanner/lesson_list.html', {})
