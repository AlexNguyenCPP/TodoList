
from django.shortcuts import render
from django.views.generic import ListView
from .models import Todo
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm


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

class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todo_detail.html'
    context_object_name = 'todo'

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
