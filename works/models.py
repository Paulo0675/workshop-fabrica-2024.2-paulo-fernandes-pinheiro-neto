#Bibliotecas de Base
from django.db import models

#Bibliotecas pra Funcionalidades
from datetime import date

# Create your models here.

#Entidade Categoria | Categoria
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Nome da Categoria:")

    def __str__(self):
        return self.name
    
#Entidade das Tarefas | Todo(Do Ingles "Para Fazer")
class Todo(models.Model):
    title = models.CharField(max_length = 255, null = False,blank = False,verbose_name = "Título:")
    created_at = models.DateField(auto_now_add = True, blank = False, null = False)
    deadline = models.DateField(blank = False,null = False)
    finished_at = models.DateField(null= True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name="todos",verbose_name="Categoria")

    class Meta:
        ordering = ['deadline']


    def completed(self):
        if not self.finished_at:
            self.finished_at = date.today()
            self.save()