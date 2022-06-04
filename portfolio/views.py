from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


from portfolio.models import PontuacaoQuizz
from portfolio.models import Post
from portfolio.models import Project
from portfolio.forms import PostForm, CourseForm, ProjectForm
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


def quizz_page_view(request):
    quizz(request)
    context = {'quizzes': Picture.objects.all()}
    return render(request, 'portfolio/quizz.html', context)


def blog_page_view(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'portfolio/blog.html', context)

def login_page_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('portfolio:home'))
        else:
            return render(request, 'portfolio/login.html', {
                'message': 'Credenciais invalidas.'
            })

    return render(request, 'portfolio/login.html')

def view_logout(request):
    logout(request)

    return render(request, 'portfolio/login.html', {
                'message': 'Foi desconetado.'
            })


def newblog_page_view(request):
    post = PostForm(request.POST or None)
    if post.is_valid():
        post.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))
    context = {'post': post}
    return render(request, 'portfolio/newBlog.html', context)

@login_required
def newcourse_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))
    course = CourseForm(request.POST or None)
    if course.is_valid():
        course.save()
        return HttpResponseRedirect(reverse('portfolio:course'))
    context = {'course': course}
    return render(request, 'portfolio/newCourse.html', context)

@login_required
def newproject_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))
    project = ProjectForm(request.POST or None)
    if project.is_valid():
        project.save()
        return HttpResponseRedirect(reverse('portfolio:projects'))
    context = {'project': project}
    return render(request, 'portfolio/newProject.html', context)


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
    plt.savefig('graf.png')

    i = Picture(image='pictures/graf.png', name="graf")
    i.save()


def quizz(request):
    if request.method == 'POST':
        n = request.POST['name']
        p = pontuacao_quizz(request)
        r = PontuacaoQuizz(name=n, score=p)
        r.save()
        desenha_grafico_resultados(request)
