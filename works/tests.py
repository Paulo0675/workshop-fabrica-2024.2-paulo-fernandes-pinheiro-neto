from django.test import TestCase

# Create your tests here.
"""
#Bibliotecas de Base e Ferramentas adicionais
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.http import HttpResponse
import requests

#Biblioteca Modelos
from .models import Todo, Category

# Configurações da API
API_BASE_URL = 'https://jsonplaceholder.typicode.com/todos'

# Create your views here.

#Modelo CLV(Class Based Views) | Do modelo Todo

class TodoListView(ListView):
    model = Todo
    template_name = 'todo_list.html'
    context_object_name = 'todos'

    def get_queryset(self):
        response = requests.get(API_BASE_URL)
        todos = response.json()
        return todos

class TodoCreateView(CreateView):
    model = Todo
    fields = ['title','deadline','category']
    success_url = reverse_lazy("todo_list")

    def form_valid(self, form):
        response = requests.post(API_BASE_URL, json=form.cleaned_data)
        if response.status_code == 201:
            return super().form_valid(form)
        return HttpResponse("Erro ao criar tarefa", status=500)

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['title', 'deadline', 'category']
    success_url = reverse_lazy("todo_list")

    def form_valid(self, form):
        todo = get_object_or_404(Todo, pk=self.kwargs['pk'])
        response = requests.put(f"{API_BASE_URL}/{todo.id}", json=form.cleaned_data)
        if response.status_code == 200:
            return super().form_valid(form)
        return HttpResponse("Erro ao atualizar tarefa", status=500)


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")

    def post(self, request, *args, **kwargs):
        todo = get_object_or_404(Todo, pk=self.kwargs['pk'])
        response = requests.delete(f"{API_BASE_URL}/{todo.id}")
        if response.status_code == 200:
            return super().post(request, *args, **kwargs)
        return HttpResponse("Erro ao excluir tarefa", status=500)

class TodoCompleteView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.completed()  

        response = requests.patch(f"{API_BASE_URL}/{todo.id}", json={"completed": True})
        if response.status_code == 200:
            return redirect("todo_list")
        return HttpResponse("Erro ao concluir tarefa", status=500)
    
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
"""
