from django.forms import ModelForm
from .models import Post
from .models import Course
from .models import Project

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
