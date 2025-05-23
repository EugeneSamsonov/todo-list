# Generated by Django 4.2.16 on 2024-11-09 07:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0003_alter_task_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='session_key',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='Дата задачи'),
        ),
        migrations.AlterField(
            model_name='task',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Категория'),
        ),
    ]
