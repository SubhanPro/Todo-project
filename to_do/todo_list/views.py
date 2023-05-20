from django.shortcuts import render, redirect
from todo_list.models import ToDoModel
from django.http import Http404

def index(request):
    if request.user.is_authenticated:
        todos = ToDoModel.objects.filter(user = request.user)
        search = request.GET.get("search")
        if search:
            todos = ToDoModel.objects.filter(user = request.user, name__contains = search)
        context = {
            'todos': todos
        }
        return render(request, 'index.html', context)
    else:
        return redirect('login')

def create(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            title = request.POST["title"]
            start_time = request.POST["start_time"]
            end_time = request.POST["end_time"]
            date = request.POST["date"]
            todo = ToDoModel.objects.create(
                name = title,
                start_time = start_time,
                end_time = end_time,
                date = date,
                user = request.user
            )
        return render(request, 'create.html')
    else:
        raise Http404