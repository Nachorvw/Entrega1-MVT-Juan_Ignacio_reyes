# Generated by Django 4.1 on 2023-01-31 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_userprofile_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='patient',
        ),
    ]
