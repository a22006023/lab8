# Generated by Django 4.0.4 on 2022-05-29 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0023_remove_course_professor_course_professor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
