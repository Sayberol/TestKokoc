# Generated by Django 4.0.6 on 2022-07-16 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='name',
        ),
        migrations.RemoveField(
            model_name='question',
            name='name',
        ),
    ]
