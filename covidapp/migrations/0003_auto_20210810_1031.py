# Generated by Django 3.2.5 on 2021-08-10 07:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('covidapp', '0002_alter_patientinput_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorsinput',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='doctorsinput',
            name='date_modified',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='patientinput',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='patientinput',
            name='date_modified',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='patientinput',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to=settings.AUTH_USER_MODEL),
        ),
    ]
