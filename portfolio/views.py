from django.shortcuts import render
from portfolio.models import PontuacaoQuizz
import matplotlib
from matplotlib import pyplot as plt

matplotlib.use('Agg')


def home_page_view(request):
    return render(request, 'portfolio/home.html')


def projetos_page_view(request):
    return render(request, 'portfolio/projects.html')


def formacao_page_view(request):
    return render(request, 'portfolio/course.html')


def competencias_page_view(request):
    return render(request, 'portfolio/skills.html')


def apresentacao_page_view(request):
    return render(request, 'portfolio/about.html')


def quizz_page_view(request):
    return render(request, 'portfolio/quizz.html')


def blog_page_view(request):
    return render(request, 'portfolio/blog.html')


def pontuacao_quizz(request):
    naosei = request.POST.getlist('question2')
    score = 0
    if request.POST['question1'] == 'print':
        score += 1
    if '+=' in naosei:
        score += 1
    if '//=' in naosei:
        score += 1
    if '%=' in naosei:
        score += 1
    if request.POST['question3'] == 'Cachapa':
        score += 1
    if request.POST['question4'] == '0.00100':
        score += 1
    if request.POST['question5'] == 'q5.4':
        score += 1
    return score


def desenha_grafico_resultados(request):
    pontuacoes = PontuacaoQuizz.objects.all()
    pontuacao_sorted = sorted(pontuacoes, key=lambda x: x.score, reverse=False)
    nameslist = []
    scorelist = []

    for person in pontuacao_sorted:
        nameslist.append(person.name)
        scorelist.append(person.score)

    plt.barh(nameslist, scorelist)
    plt.savefig('portfolio/static/portfolio/images/graf.png', bbox_inches='tight')


def quizz(request):
    if request.method == 'POST':
        n = request.POST['name']
        p = pontuacao_quizz(request)
        r = PontuacaoQuizz(name=n, score=p)
        r.save()
        desenha_grafico_resultados(request)
    return render(request, 'portfolio/quizz.html')
