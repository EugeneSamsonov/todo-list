from django.db import models
from django.utils import timezone

# Create your models here.
from users.models import TaskUser

class Task(models.Model):
    user = models.ForeignKey(to=TaskUser, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Категория")
    text = models.TextField(verbose_name="Текст задачи")
    date = models.DateField(default=timezone.now, verbose_name="Дата задачи")
    is_done = models.BooleanField(default=False, verbose_name="Выполнено")
    session_key = models.CharField(max_length=32, null=True, blank=True)

    class Meta:
        db_table = 'task'
        verbose_name = "задача"
        verbose_name_plural = "Задачи"
        ordering = ("id", )

    def __str__(self):
        return f"{self.user.username if self.user else 'null'}: {self.text[:10]} | {self.date} | {self.is_done}"