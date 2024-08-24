"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#Bibliotecas de Base
from django.contrib import admin
from django.urls import path

#Bibliotecas e Estruturas Externas
from works.views import TodoCreateView,TodoListView,TodoUpdateView,TodoDeleteView,TodoCompleteView
from works.views import CategoryCreateView,CategoryListView,CategoryUpdateView,CategoryDeleteView

urlpatterns = [
    #Paths da Classe Todo
    path('admin/', admin.site.urls),
    path('', TodoListView.as_view(),name="todo_list"),
    path('create', TodoCreateView.as_view(), name="todo_create"),
    path('update/<int:pk>', TodoUpdateView.as_view(),name="todo_update"),
    path('delete/<int:pk>', TodoDeleteView.as_view(),name="todo_delete"),
    path('complete/<int:pk>', TodoCompleteView.as_view(),name="todo_complete"),

    #Paths da Classe Category
    path('categories/', CategoryListView.as_view(), name="category_list"),
    path('categories/create/', CategoryCreateView.as_view(), name="category_create"),
    path('categories/update/<int:pk>/', CategoryUpdateView.as_view(), name="category_update"),
    path('categories/delete/<int:pk>/', CategoryDeleteView.as_view(), name="category_delete"),
]

