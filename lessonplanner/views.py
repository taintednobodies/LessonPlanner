from django.utils import timezone
from .models import Lesson
from django.shortcuts import render, get_object_or_404
from .forms import LessonForm
from django.shortcuts import redirect
from django.db.models import Q
import operator


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

def lesson_search(request):
    query_string = ''
    
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        
        entry_query = get_query(query_string, ['chapter'])

        lessons = Lesson.objects.order_by('className')

        found_entries = lessons 

        
        for lesson in lessons:
            if query_string in lesson.chapter:
                found_entries.append(lesson)
        
        
  #      found_entries = Lesson.objects.filter(entry_query).order_by('chapter')

    return render ('lessonplanner/lesson_search.html',
                          { 'query_string': query_string, 'found_entries': found_entries })



import re
from django.db.models import Q


def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:
        
        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']
    
    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)] 

def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.
    
    '''
    query = None # Query to search for every search term        
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query
