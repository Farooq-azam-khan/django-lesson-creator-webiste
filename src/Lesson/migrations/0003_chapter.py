# Generated by Django 2.0.5 on 2018-06-04 05:08

import Lesson.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Lesson', '0002_auto_20180604_0108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_title', models.CharField(max_length=120, unique=True)),
                ('owner', models.ForeignKey(default=1, on_delete=models.SET(Lesson.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]