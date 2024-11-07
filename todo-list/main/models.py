from django.db import models

# Create your models here.
from users.models import TaskUser

class Task(models.Model):
    user = models.ForeignKey(to=TaskUser, on_delete=models.CASCADE, verbose_name="Категория")
    text = models.TextField(verbose_name="Текст задачи")
    date = models.DateField(auto_now=True, auto_now_add=False, verbose_name="Дата задачи")
    is_done = models.BooleanField(default=False, verbose_name="Выполнено")

    class Meta:
        db_table = 'task'
        verbose_name = "задача"
        verbose_name_plural = "Задачи"
        ordering = ("id", )

    def __str__(self):
        return f"{self.user.username}: {self.text[:10]} | {self.date} | {self.is_done}"