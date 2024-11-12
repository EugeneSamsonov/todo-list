# Generated by Django 4.2.16 on 2024-11-09 14:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_alter_task_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата задачи'),
        ),
    ]
