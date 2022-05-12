# Generated by Django 3.1 on 2022-05-12 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20220511_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='occupation',
            field=models.CharField(choices=[('professor', 'Professor'), ('other', 'Other'), ('manager', 'Manager'), ('student', 'Student'), ('consultant', 'Consultant')], default='student', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=10),
        ),
    ]
