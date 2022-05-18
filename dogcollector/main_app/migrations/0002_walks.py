# Generated by Django 4.0.4 on 2022-05-18 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Walks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('P', 'Park'), ('N', 'Neighbourhood'), ('L', 'Lakeside')], default='P', max_length=1)),
                ('date', models.DateField(verbose_name='Walk date')),
                ('pooped', models.BooleanField(default=False)),
            ],
        ),
    ]
