from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^todos/$',
        views.TodoList.as_view(),
        name='todo_list'),

    url(r'^todos/complete/$',
        views.TodoList.as_view(),
        name='complete_todo_list'),

    url(r'^todos/incomplete/$',
        views.TodoList.as_view(),
        name='incomplete_todo_list'),

    url(r'^todo/(?P<pk>\d+)/$',
        views.TodoDetail.as_view(),
        name='todo_detail'),

    url(r'^todo/create/$',
        views.TodoCreate.as_view(),
        name='todo_create'),

    url(r'^todo/edit/(?P<pk>\d+)/$',
        views.TodoUpdate.as_view(),
        name='todo_update'),

    url(r'^todo/delete/(?P<pk>\d+)/$',
        views.TodoDelete.as_view(),
        name='todo_delete'),
]
