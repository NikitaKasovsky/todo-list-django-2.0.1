from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django import forms # импорт django форм
from django.template import RequestContext 
from todo.forms import add_task_form, add_list_form, view_task, view_list # импорт форм представления
from todo import models 
from todo.models import task, List
# функция рендера основной страницы
def home(request):
	return render(request, 'home.html')
# функция создания нового листа (категории)
def new_list(request):
	if request.method == 'POST': # определения метода запроса
		form = add_list_form(request.POST) # указываем на использование формы(с использованным методом)
		if form.is_valid(): # проверка формы на корректно введеные данные
			post_l = form.save(commit = False) # сохраняем введенные данные
			post_l.save()
			return redirect('tree_objects')
	else:
		form = add_list_form()
	return render(request, 'new_list.html', {'form': form})  
# выборка всех объектов из моделей
def get_objects(request):
	vars = dict (
		tasks=task.objects.all().order_by('lisst_id'), # выборка задач
		lists=List.objects.all().order_by('id'), # выорка всех листов(категории по FK)
	)
	return render_to_response('tree_objects.html', vars, RequestContext(request)) # рендерит указанный шаблон с указанным контекстом (все дерево объектов из модели) 
# функция вывода содержимого задачи и ее перезаписи
def select_task(request, task_id):
    post = get_object_or_404(task, pk=task_id) # выбор записи в модели по pk
    if request.method == "POST": # определения метода запроса
        form = view_task(request.POST, instance=post) # указываем на использование определенной формы с выбранной записью из модели
        if form.is_valid(): # проверка формы на корректно введеные данные
            post = form.save(commit=False) # сохраняем
            post.save()
            return redirect('tree_objects')
    else:
        form = view_task(instance=post)
    return render(request, 'one_task.html', {'form': form})
# функция удаления задачи
def delete_task(request, task_id):
	object = get_object_or_404(task, pk=task_id) # выбор записи в модели по pk
	object.delete() 
	return redirect('tree_objects')
# функция изменения состояния задачи (пометка выполненной/невыполненной задачи)
def toggle_task(request, task_id):
	object = get_object_or_404(task, pk=task_id) # выбор записи в модели по pk
	object.is_done = not object.is_done 
	object.save()
	return redirect('tree_objects')
# функция вывода содержимого листа(категории) и его изменения
def select_list(request, list_id):
    post = get_object_or_404(List, pk=list_id) # выбор записи в модели по pk
    if request.method == "POST": # определения метода запроса
        form = view_list(request.POST, instance=post) # выбор формы
        if form.is_valid(): # проверка формы на корректно введеные данные
            post = form.save(commit=False) # сохраняем
            post.save()
            return redirect('tree_objects')
    else:
        form = view_list(instance=post)
    return render(request, 'one_list.html', {'form': form})
# функция удаления листа (категрии)
def delete_list(request, list_id):
	object = get_object_or_404(List, pk=list_id) # выбор записи в модели по pk
	object.delete()
	return redirect('tree_objects')
# функция создания новой задачи
def new_task(request):
	if request.method == 'POST': # определения метода запроса
		form = add_task_form(request.POST) # выбор формы
		if form.is_valid(): # проверка формы на корректно введеные данные
			post_t = form.save(commit = False) # сохраняем
			post_t.save()
			return redirect('tree_objects')
	else:
		form = add_task_form()
	return render(request, 'new_task.html', {'form': form})