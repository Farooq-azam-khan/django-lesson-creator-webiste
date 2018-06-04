# Generated by Django 2.0.5 on 2018-06-04 05:13

import Lesson.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Lesson', '0005_chaptermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.CharField(max_length=120)),
                ('section_content', models.TextField(help_text='Write your content here.')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lesson.ChapterModel')),
                ('owner', models.ForeignKey(default=1, on_delete=models.SET(Lesson.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
