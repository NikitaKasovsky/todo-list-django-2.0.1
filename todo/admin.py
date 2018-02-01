from django.contrib import admin
from .models import task, List

admin.site.register(task) # подключение модели task
admin.site.register(List) # подключение модели List