from django.db import models

from users.models import User


class Habit(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Владелец", help_text="Укажите владельца", related_name="habits")
    place = models.CharField(max_length=100, null=True, blank=True, verbose_name="Место", help_text="Укажите место для выполения привычки")
    time = models.TimeField(null=True, blank=True, verbose_name="Время", help_text="Укажите время для выполения привычки")
    action = models.CharField(max_length=200, verbose_name="Действие", help_text="Укажите действие, которое представляет собой привычка")
    is_pleasant_habit = models.BooleanField(verbose_name="Признак приятной привычки", help_text="Укажите, является ли привычка приятной")
    associated_habit = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Связанная привычка", help_text="Укажите связанную привычку")
    periodicity = models.SmallIntegerField(default=1, verbose_name="Периодичность", help_text="Укажите периодичность выполнения привычки, раз в 7 дней")
    reward = models.CharField(max_length=200, null=True, blank=True, verbose_name="Вознаграждение", help_text="Укажите вознаграждение после выполнения привычки")
    duration = models.PositiveIntegerField(null=True, blank=True, verbose_name="Продолжительность выполнения в секундах", help_text="Укажите продолжительность выполнения привычки в секундах")
    is_published = models.BooleanField(verbose_name="Признак публикации", help_text="Укажите, необходимо ли публикация")

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
        ordering = [
            "action",
            "periodicity",
            "is_published",
        ]

    def __str__(self):
        return self.action
