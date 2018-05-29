# Generated by Django 2.0.5 on 2018-05-29 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lesson', '0011_auto_20180528_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonplan',
            name='subtitle',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='lessonplan',
            name='lesson_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]