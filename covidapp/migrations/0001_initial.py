# Generated by Django 3.2.5 on 2021-08-03 10:34

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, default='Add Bio....', max_length=255)),
                ('name', models.CharField(blank=True, max_length=60)),
                ('location', models.CharField(blank=True, max_length=60)),
                ('profile_pic', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
