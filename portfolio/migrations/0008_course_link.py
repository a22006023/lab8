# Generated by Django 4.0.4 on 2022-05-28 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_course_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='link',
            field=models.URLField(blank=True),
        ),
    ]
