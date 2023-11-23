from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Todo
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')

class TodoListView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = 'todo_list.html'
    context_object_name = 'todos'
    login_url = '/accounts/login/' # redirect to this URL if not logged in
    redirect_field_name = 'redirect_to'

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user).order_by('-created_date')
class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ['title', 'description', 'completed', 'due_date']
    template_name = 'todo_form.html'
    success_url = reverse_lazy('todo_list')

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
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

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})