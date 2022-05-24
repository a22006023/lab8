from django.db import models

# Create your models here.
class PontuacaoQuizz(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField()

    def str(self):
        return self.name[:50]
