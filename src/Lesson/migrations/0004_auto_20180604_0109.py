# Generated by Django 2.0.5 on 2018-06-04 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lesson', '0003_chapter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Chapter',
        ),
    ]
