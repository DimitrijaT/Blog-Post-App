# Generated by Django 4.2.1 on 2023-06-01 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloguser',
            name='image',
        ),
        migrations.RemoveField(
            model_name='bloguser',
            name='interests',
        ),
        migrations.RemoveField(
            model_name='bloguser',
            name='profession',
        ),
        migrations.RemoveField(
            model_name='bloguser',
            name='skills',
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
