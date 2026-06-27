from . import models
from django.views.generic import ListView, DetailView

# Create your views here.
class TodoListView(ListView):
    model = models.Todo
    template_name = 'todoapp/todo_list.html'
    context_object_name = 'todos'

class TodoDetailView(DetailView):
    model = models.Todo
    templete_name = 'todoapp/todo_detail.html'
    context_object_name = 'todo'
