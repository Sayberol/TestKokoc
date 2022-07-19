# Generated by Django 4.0.6 on 2022-07-16 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('text', models.TextField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('text', models.TextField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('right_answer', models.BooleanField(default=False)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.question')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='questions',
            field=models.ManyToManyField(through='tests.QuestionAnswer', to='tests.question'),
        ),
    ]