from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.TodoListView.as_view(), name='todo_list'),
    path('<int:pk>/', views.TodoDetailView.as_view(), name='todo_detail'),
    path('new/', views.TodocreateView.as_view(), name='todo_create'),
]