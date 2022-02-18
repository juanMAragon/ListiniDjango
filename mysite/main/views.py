from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import toDoList, Item
from .forms import CreateNewList

# Create your views here.
def index(response, id):
    ls = toDoList.objects.get(id=id)

    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == 'clicked':
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        elif response.POST.get("newItem"):
            txt = response.POST.get('new')

            if len(txt) > 1:
                ls.item_set.create(text=txt, complete=False)
            else:
                print('invalid')

    return render(response, "main/list.html", {"name":'list', "ls":ls})

def home(response):
    return render(response, 'main/home.html', {"name":'home'})

def create(response):

    if response.method == 'POST':
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data['name']
            t = toDoList(name=n)
            t.save()
        
        return HttpResponseRedirect(f'/{t.id}')
    else:
        form = CreateNewList()
        return render(response, 'main/create.html', {"name":"create", "form":form})