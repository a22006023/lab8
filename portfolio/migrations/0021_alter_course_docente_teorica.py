# Generated by Django 4.0.4 on 2022-05-29 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0020_course_docente_teorica'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='docente_teorica',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.person'),
        ),
    ]
