from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.lesson_list, name='lesson_list'),
    url(r'^lesson/(?P<pk>\d+)/$', views.lesson_detail, name='lesson_detail'),
]
