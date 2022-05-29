from django.contrib import admin

# Register your models here.
from .models import PontuacaoQuizz
from .models import Post
from .models import Project
from .models import Person
from .models import Course
from .models import Picture

admin.site.register(PontuacaoQuizz)
admin.site.register(Post)
admin.site.register(Project)
admin.site.register(Person)
admin.site.register(Course)
admin.site.register(Picture)
