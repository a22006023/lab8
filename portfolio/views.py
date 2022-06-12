from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


from portfolio.models import PontuacaoQuizz
from portfolio.models import Post
from portfolio.models import Project
from portfolio.forms import PostForm, CourseForm, ProjectForm, PersonForm
from portfolio.models import Course
import urllib
from urllib.parse import urlparse
import base64
import io
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
    context = {'data': desenha_grafico_resultados()}
    return render(request, 'portfolio/quizz.html', context)


def view_weather(request):
    return render(request, 'portfolio/weather.html')

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
    return HttpResponseRedirect(reverse('portfolio:home'))


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
    context = {'course': course, 'view': 'newCourse'}
    return render(request, 'portfolio/newCourse.html', context)

@login_required
def newproject_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))
    project = ProjectForm(request.POST, request.FILES or None)
    if project.is_valid():
        project.save()
        return HttpResponseRedirect(reverse('portfolio:projects'))
    context = {'project': project}
    return render(request, 'portfolio/newProject.html', context)


@login_required
def view_editar_course(request, course_id):

    course = Course.objects.get(id=course_id)
    form = CourseForm(request.POST or None, instance=course)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:course'))

    context = {'form': form, 'course_id': course_id}
    return render(request, 'portfolio/editCourse.html', context)

@login_required
def view_editar_project(request, project_id):

    project = Project.objects.get(id=project_id)
    form = ProjectForm(request.POST or None, instance=project)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projects'))
    context = {'form': form, 'project_id': project_id}
    return render(request, 'portfolio/editProject.html', context)

def view_delete_project(request, project_id):

    project = Project.objects.get(id=project_id)
    project.delete()
    return HttpResponseRedirect(reverse('portfolio:projects'))

def view_apagar_course(request, course_id):

    course = Course.objects.get(id=course_id)
    course.delete()
    return HttpResponseRedirect(reverse('portfolio:course'))

def view_apagar_blog(request, blog_id):

    blog = Post.objects.get(id=blog_id)
    blog.delete()
    return HttpResponseRedirect(reverse('portfolio:blog'))

def newperson_page_view(request):
    person = PersonForm(request.POST or None)
    if person.is_valid():
        person.save()
        return HttpResponseRedirect(reverse('portfolio:newCourse'))
    context = {'course': person, 'view': 'newPerson'}
    return render(request, 'portfolio/newCourse.html', context)

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


def desenha_grafico_resultados():
    pontuacoes = PontuacaoQuizz.objects.all().order_by('score')

    nameslist = [pontuacao.name for pontuacao in pontuacoes]
    scorelist = [pontuacao.score for pontuacao in pontuacoes]

    plt.barh(nameslist, scorelist)
    plt.ylabel("Score")
    plt.autoscale()

    fig = plt.gcf()
    plt.close()

    buf = io.BytesIO()
    fig.savefig(buf, format='png')

    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    return uri

def quizz(request):
    if request.method == 'POST':
        n = request.POST['name']
        p = pontuacao_quizz(request)
        r = PontuacaoQuizz(name=n, score=p)
        r.save()
