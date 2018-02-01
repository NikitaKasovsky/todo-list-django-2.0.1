from todo.models import task, List # импорт моделей
from django import forms
from todo import views

class add_task_form(forms.ModelForm): # форма для создания задачи
	class Meta():
		model = task # указываем модель 
		fields = [ # указываем поля
			'title',
			'area',
			'lisst',
		]
		widgets = { # определяем вид выводимых полей для шаблона
			'title':forms.TextInput(attrs={'placeholder':'Название задачи','class':'form-control'}),
			'area':forms.Textarea(attrs={'placeholder':'Описание задачи','class':'form-control'}),
			'lisst':forms.RadioSelect(), 
		}
		labels = { # корректируем название полей для шаблона
			'title': 'Название задачи',
			'area': 'Текст',
			'lisst': 'Категория'
		}

class add_list_form(forms.ModelForm): #  форма для создания листа (категории)
	class Meta():
		model = List
		fields = [
			'list_title',
		]
		widgets = {
			'list_title':forms.TextInput(attrs={'placeholder':'Название категории','class':'form-control'}),
		}
		labels = {
			'list_title': 'Название листа'
		}

class view_task(forms.ModelForm): # форма для визуализации данных модели task
	class Meta():
		model = task
		fields = [
			'title',
			'area',
			'lisst',
			'is_done'
		]
		widgets = {
			'title':forms.TextInput(attrs={'placeholder':'Название задачи','class':'form-control'}),
			'area':forms.Textarea(attrs={'placeholder':'Описание задачи','class':'form-control'}),
			'lisst':forms.RadioSelect(),
			'is_done':forms.CheckboxInput(),
		}
		labels = {
			'title': 'Название задачи',
			'area': 'Текст',
			'lisst': 'Категория',
			'is_done': 'Задача выполнена?'
		}

class view_list(forms.ModelForm): # Форма для визуализации данных модели List
	class Meta():
		model = List
		fields = [
			'list_title',
		]
		widgets = {
			'list_title':forms.TextInput(attrs={'placeholder':'Название категории','class':'form-control'}),
		}
		labels = {
			'list_title': 'Название листа'
		}