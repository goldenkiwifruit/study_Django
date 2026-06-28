from . import models
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.utils.timezone import localtime
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

class TodoCreateView(CreateView):
    model = models.Todo
    template_name = 'todoapp/todo_create.html'
    fields = ['title', 'memo', 'completed']
    success_url = reverse_lazy('todo_list')

class TodoUpdateView(UpdateView):
    model = models.Todo
    template_name = 'todoapp/todo_update.html'
    fields = ['title', 'memo', 'completed']
    success_url = reverse_lazy('todo_list')

    def form_valid(self, form):
        todo = form.save()
        print(f"タィトル:'{todo.title}' 更新時間:{localtime(todo.updated)}")
        return super().form_valid(form)

class TodoDeleteView(DeleteView):
    model = models.Todo
    template_name = 'todoapp/todo_confirm.html'
    success_url = reverse_lazy('todo_list')
