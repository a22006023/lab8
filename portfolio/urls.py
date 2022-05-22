from . import views
from django.urls import path

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('projects', views.projetos_page_view, name='projects'),
    path('course', views.formacao_page_view, name='course'),
    path('skills', views.competencias_page_view, name='skills'),
    path('about', views.apresentacao_page_view, name='about'),
    path('quizz', views.quizz, name='quizz'),
    path('blog', views.blog_page_view, name='blog'),
]