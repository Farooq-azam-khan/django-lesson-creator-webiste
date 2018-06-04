# Generated by Django 2.0.5 on 2018-06-04 05:06

import Profile.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('owner', models.ForeignKey(on_delete=models.SET(Profile.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
