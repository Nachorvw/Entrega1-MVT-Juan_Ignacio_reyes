# Generated by Django 4.1 on 2023-02-05 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Consultorio', '0010_media'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='media',
            options={'verbose_name': 'Media', 'verbose_name_plural': 'Media'},
        ),
        migrations.RenameField(
            model_name='media',
            old_name='Img',
            new_name='media_img',
        ),
    ]