from . import views
from django.urls import path


app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('projects', views.projetos_page_view, name='projects'),
    path('course', views.formacao_page_view, name='course'),
    path('quizz', views.quizz_page_view, name='quizz'),
    path('blog', views.blog_page_view, name='blog'),
    path('newBlog', views.newblog_page_view, name='newBlog'),
    path('editBlog/<int:post_id>', views.edit_page_view, name='editBlog'),
    path('login', views.login_page_view, name='login'),
    path('newProject', views.newproject_page_view, name='newProject'),
    path('newCourse', views.newcourse_page_view, name='newCourse'),
    path('logout', views.view_logout, name="logout"),
    path('editCourse/<int:course_id>', views.view_editar_course, name='editCourse'),
    path('deleteCourse/<int:course_id>', views.view_apagar_course, name='deleteCourse'),
    path('newPerson', views.newperson_page_view, name='newPerson'),
    path('editProject/<int:project_id>', views.view_editar_project, name='editProject'),
    path('deleteBlog/<int:blog_id>', views.view_apagar_blog, name="deleteBlog"),
    path('deleteProjects/<int:project_id>', views.view_delete_project, name='deleteProject'),
]

