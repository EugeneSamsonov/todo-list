# Generated by Django 4.2.16 on 2024-11-07 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст задачи')),
                ('date', models.DateField(verbose_name='Дата задачи')),
                ('is_done', models.BooleanField(default=False, verbose_name='Выполнено')),
            ],
            options={
                'verbose_name': 'задача',
                'verbose_name_plural': 'Задачи',
                'db_table': 'task',
                'ordering': ('id',),
            },
        ),
    ]
