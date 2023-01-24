# Generated by Django 4.1 on 2023-01-23 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Consultorio', '0008_alter_orders_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(blank=True, null=True)),
                ('dni', models.IntegerField(blank=True, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('affiliate_code', models.IntegerField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=25, null=True)),
                ('profile_img', models.ImageField(blank=True, null=True, upload_to='profile_images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='Consultorio.patient')),
            ],
        ),
    ]