# Generated by Django 2.0.5 on 2018-05-29 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lesson', '0020_auto_20180529_0431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='chapter_title',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
