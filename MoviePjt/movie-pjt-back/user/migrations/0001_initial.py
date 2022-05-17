# Generated by Django 3.1 on 2022-05-17 08:21

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('kakao_id', models.BigIntegerField(unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(blank=True, max_length=8, null=True)),
                ('register_date', models.DateField(auto_now_add=True)),
                ('is_valid', models.BooleanField(default=True)),
                ('unregister_date', models.DateField(default=None)),
                ('refresh_token', models.CharField(max_length=64)),
            ],
        ),
    ]
