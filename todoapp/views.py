from . import models
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

# Create your views here.
class TodoListView(ListView):
    model = models.Todo
    template_name = 'todoapp/todo_list.html'
    context_object_name = 'todos'

class TodoDetailView(DetailView):
    model = models.Todo
    templete_name = 'todoapp/todo_detail.html'
    context_object_name = 'todo'

class TodocreateView(CreateView):
    model = models.Todo
    template_name = 'todoapp/todo_create.html'
    fields = ['title', 'memo', 'completed']
    success_url = reverse_lazy('todo_list')
