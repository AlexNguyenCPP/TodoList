
from django.shortcuts import render
from django.views.generic import ListView
from .models import Todo
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def home(request):
    return render(request, 'home.html')

class TodoListView(ListView):
    model = Todo
    template_name = 'todo_list.html'
    context_object_name = 'todos'

class TodoCreateView(CreateView):
    model = Todo
    fields = ['title', 'description', 'completed', 'due_date']
    template_name = 'todo_form.html'
    success_url = reverse_lazy('todo_list')

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['title', 'description', 'completed', 'due_date']
    template_name = 'todo_form.html'
    success_url = reverse_lazy('todo_list')

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todo_confirm_delete.html'
    success_url = reverse_lazy('todo_list')
