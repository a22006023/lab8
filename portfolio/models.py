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
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.author

class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio/static/portfolio/images')

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
    semester = models.IntegerField(default=1)
    professor = models.ManyToManyField(Person)
    description = models.CharField(max_length=130)
    ects = models.IntegerField(default=0)
    link = models.URLField(blank=True, null=True, default='')

    def __str__(self):
        return self.title
