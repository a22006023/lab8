from django.db import models

# Create your models here.
class PontuacaoQuizz(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name[:50]


class Post(models.Model):
    author = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.author

class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to="pictures/")

    def __str__(self):
        return self.title

class Person(models.Model):
    name = models.CharField(max_length=30)
    linkedIn = models.URLField(blank=True, default='')

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=30)
    rank = models.IntegerField(default=1)
    year = models.IntegerField(default=1)
    professor = models.ForeignKey(Person, related_name='Course', on_delete=models.CASCADE, default='')
    semester = models.IntegerField(default=1)
    ects = models.IntegerField(default=0)
    link = models.URLField(blank=True, null=True, default='')
    description = models.CharField(max_length=130)

    def __str__(self):
        return self.title


class Picture(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pictures/', blank=True)

    def __str__(self):
        return self.name
