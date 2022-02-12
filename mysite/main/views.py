from django.shortcuts import render
from django.http import HttpResponse
from .models import toDoList, Item

# Create your views here.
def index(response, id):
    ls = toDoList.objects.get(id=id)
    item = ls.item_set.get(id=1)
    return HttpResponse(f"<h1>Hello world {ls.name} -> {item.text}</h1>")
