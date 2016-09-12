from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.lesson_list, name='lesson_list'),
]
