# Generated by Django 3.2.5 on 2021-08-09 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('covidapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientinput',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]