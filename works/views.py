#Bibliotecas de Base e Ferramentas adicionais
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy

#Biblioteca Modelos
from .models import Todo, Category

# Create your views here.

#Modelo CLV(Class Based Views) | Do modelo Todo

class TodoListView(ListView):
    model = Todo
    template_name = 'todo_list.html'
    context_object_name = 'todos'

class TodoCreateView(CreateView):
    model = Todo
    fields = ['title','deadline','category']
    success_url = reverse_lazy("todo_list")
    #template_name = ".html"

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['title', 'deadline', 'category']
    success_url = reverse_lazy("todo_list")
    #template_name = ".html"

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")
    #template_name = ".html"

class TodoCompleteView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)  # Obtém um único objeto Todo
        todo.completed()  # Chama o método mark_has_complete
        return redirect("todo_list")
    
#Modelo CLV(Class Based Views) | Do modelo Categoria

class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'

class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']
    success_url = reverse_lazy("category_list")
    #template_name = ".html"

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name']
    success_url = reverse_lazy("category_list")
    #template_name = ".html"

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy("category_list")
    #template_name = ".html"
