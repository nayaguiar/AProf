from django.db import models

# Create your models here.

class Curso(models.Model):
    nome = models.CharField(max_length=50)
    carga_horaria = models.TimeField()
    ementa = models.CharField(max_length=100)
    valor = models.IntegerField(max_length=10)

    def __str__(self):
        return self.nome

class Turma(models.Model):
    data_inicio = models.DateField()
    data_termino = models.DateField()
    hora_inicio = models.TimeField()
    hora_termino = models.TimeField()

    def __str__(self):
        return self.data_inicio

class Professor(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)
    valor_hora_aula = models.IntegerField()

    def __str__(self):
        return self.nome


