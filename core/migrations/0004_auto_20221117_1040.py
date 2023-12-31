# Generated by Django 3.2.16 on 2022-11-17 05:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_auto_20221117_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='inversterprofile',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='inversterprofile',
            name='dob',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='inversterprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='inversterprofile',
            name='fname',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='inversterprofile',
            name='id_proff',
            field=models.FileField(blank=True, upload_to='profileid/'),
        ),
        migrations.AlterField(
            model_name='inversterprofile',
            name='lname',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='inversterprofile',
            name='org',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='inversterprofile',
            name='phone',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='inversterprofile',
            name='profile',
            field=models.ImageField(blank=True, upload_to='profile/'),
        ),
        migrations.AlterField(
            model_name='inversterprofile',
            name='social_media',
            field=models.URLField(blank=True, default=''),
        ),
    ]
