from django.contrib import admin

from .models import toDoList, Item
# Register your models here.


admin.site.register(toDoList)
admin.site.register(Item)