from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


# Create your views here.


def index(request):

    todos = Todo.objects.all()


    return render(request, 'index.html', {
        "todos": todos
    })

def add(request):
    print(request.method)
    if request.method == 'POST':
        form = TodoForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            todo = Todo()
            todo.text = form.cleaned_data['text']
            todo.save()
             
    
    return redirect('home')
    
def remove(request, todo_id):
    todo = Todo.objects.get(id =todo_id)
    print(todo.text)
    todo.delete()

    return redirect('home')


def test(request):
    pass
