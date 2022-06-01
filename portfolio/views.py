import numpy as np
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from portfolio.models import PontuacaoQuizz
from portfolio.models import Post
from portfolio.models import Project
from portfolio.forms import PostForm
from portfolio.models import Course
from portfolio.models import Picture
import matplotlib
from matplotlib import pyplot as plt

matplotlib.use('Agg')


def home_page_view(request):
    return render(request, 'portfolio/home.html')


def projetos_page_view(request):
    context = {'projects': Project.objects.all()}
    return render(request, 'portfolio/projects.html', context)


def formacao_page_view(request):
    context = {'courses': Course.objects.all()}
    return render(request, 'portfolio/course.html', context)


def competencias_page_view(request):
    return render(request, 'portfolio/skills.html')


def apresentacao_page_view(request):
    return render(request, 'portfolio/about.html')


def quizz_page_view(request):
    quizz(request)
    context = {'quizzes': Picture.objects.all()}
    return render(request, 'portfolio/quizz.html', context)


def blog_page_view(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'portfolio/blog.html', context)


def newblog_page_view(request):
    post = PostForm(request.POST or None)
    if post.is_valid():
        post.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))
    context = {'post': post}
    return render(request, 'portfolio/newBlog.html', context)


def edit_page_view(request, post_id):
    post = Post.objects.get(pk=post_id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form, 'post_id': post_id}
    return render(request, 'portfolio/edit.html', context)

def pontuacao_quizz(request):
    postlist = request.POST
    q2list = request.POST.getlist('question2')
    score = 0
    if 'question1' in postlist and request.POST['question1'] == 'print':
        score += 1
    if '+=' in q2list:
        score += 1
    if '//=' in q2list:
        score += 1
    if '%=' in q2list:
        score += 1
    if '**' in q2list and score != 0:
        score -= 1
    if '++' in q2list and score != 0:
        score -= 1
    if request.POST['question3'] == 'Cachapa':
        score += 1
    if request.POST['question4'] == '0.00100':
        score += 1
    if 'question5' in postlist and request.POST['question5'] == 'q5.4':
        score += 1
    return score


def desenha_grafico_resultados(request):
    pontuacoes = PontuacaoQuizz.objects.all()
    pontuacao_sorted = sorted(pontuacoes, key=lambda x: x.score, reverse=True)
    nameslist = []
    scorelist = []

    for person in pontuacao_sorted:
        nameslist.append(person.name)
        scorelist.append(person.score)

    plt.barh(nameslist, scorelist)
    a = plt.savefig('graf.png')
    i = Picture(image=a, name="graf")
    i.save()


def quizz(request):
    if request.method == 'POST':
        n = request.POST['name']
        p = pontuacao_quizz(request)
        r = PontuacaoQuizz(name=n, score=p)
        r.save()
        desenha_grafico_resultados(request)
