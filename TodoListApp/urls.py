from django.urls import path
from .views import home, TodoListView, TodoCreateView, TodoUpdateView, TodoDeleteView

urlpatterns = [
    path('', TodoListView.as_view(), name='todo_list'),
    path('todo/add/', TodoCreateView.as_view(), name='todo_create'),
    path('todo/<int:pk>/edit/', TodoUpdateView.as_view(), name='todo_update'),
    path('todo/<int:pk>/delete/', TodoDeleteView.as_view(), name='todo_delete'),
]