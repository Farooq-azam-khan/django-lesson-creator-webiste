# Generated by Django 2.0.5 on 2018-05-29 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lesson', '0008_auto_20180528_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonplan',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]