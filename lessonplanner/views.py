from django.utils import timezone
from .models import Lesson
from django.shortcuts import render, get_object_or_404
from .forms import LessonForm
from django.shortcuts import redirect
from django.db.models import Q
import operator

# Create your views here.

class BlogSearchListView(Lesson):
    """
    Display a Blog List page filtered by the search query.
    """
    paginate_by = 10

    def get_queryset(self):
        result = super(BlogSearchListView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(summary__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(description__icontains=q) for q in query_list))
            )

        return result

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
