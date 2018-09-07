from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.notes, name='notes_list'),
    url(r'^note/(?P<pk>\d+)/$', views.note_selected, name='note_selected'),

]
