# Generated by Django 4.0.4 on 2022-05-18 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_walks_dog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='walks',
            name='pooped',
        ),
    ]
