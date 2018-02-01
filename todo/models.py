from django.db import models

class List(models.Model): # Модель листа (категории)
	class Meta():
		db_table = 'List'
	list_title = models.CharField(max_length = 100) # Название

	def __str__(self): # функция для корректного вывода названия листа (категории)
		return self.list_title

class task(models.Model): # модель задачи
	class Meta():
		db_table = 'task'
	title = models.CharField(max_length = 100) # Название задачи
	area = models.TextField() # Поле задачи
	is_done = models.BooleanField(default=False) # Cостояние задачи (выполнено/не выполнено)
	lisst = models.ForeignKey(List, on_delete=models.CASCADE) # Внешний ключ 

	def __str__(self): # функция для корректного вывода названия задачи
		return self.title