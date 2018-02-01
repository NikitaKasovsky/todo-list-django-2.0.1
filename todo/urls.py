from django.urls import path
from django.conf.urls import url
from todo import views
from django import forms
from django.http import HttpResponse

urlpatterns = [
	path('home/', views.home, name='home'), # указываем домашнюю станичку 
	#lists 
	url(r'^home/new_list$', views.new_list, name='new_list'), # создание нового листа(категории)
	url(r'^home/tree_objects/list(?P<list_id>\d+)$', views.select_list, name='one_list'), # выбор листа и его рендер(категрии)
	url(r'^home/tree_objects/list(?P<list_id>\d+)/delete_list$', views.delete_list, name='delete_list'), # удаление листа (категрии)
	#tasks
	url(r'^home/new_task$', views.new_task, name='new_task'), # создание новой задачи
	url(r'^home/tree_objects$', views.get_objects, name='tree_objects'), # каскадный вывод всех листов и вложенных в них задач
	url(r'^home/tree_objects/task(?P<task_id>\d+)$', views.select_task, name='one_task'), # выбор задачи и ее рендер
	url(r'^home/tree_objects/task(?P<task_id>\d+)/delete_task$', views.delete_task, name='delete_task'), # удаление задачи
	url(r'^home/tree_objects/task(?P<task_id>\d+)/toggle_task$', views.toggle_task,  name='toggle_task'), # пометка задачи как выполненной или же в процессе выполнения
]