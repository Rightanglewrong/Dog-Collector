# Generated by Django 4.0.4 on 2022-05-20 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_friend'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='friends',
            field=models.ManyToManyField(to='main_app.friend'),
        ),
    ]
