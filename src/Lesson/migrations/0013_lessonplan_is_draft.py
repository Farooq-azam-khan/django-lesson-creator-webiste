# Generated by Django 2.0.5 on 2018-05-29 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lesson', '0012_auto_20180529_0045'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonplan',
            name='is_draft',
            field=models.BooleanField(default=True),
        ),
    ]
