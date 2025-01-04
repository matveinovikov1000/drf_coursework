from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(
        unique=True, verbose_name="Email", help_text="Укажите ваш Email"
    )
    phone_number = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name="Номер телефона",
        help_text="Укажите ваш номер телефона",
    )
    citi = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Город",
        help_text="Укажите город пребывания",
    )
    tg_chat_id = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Телеграм chat-id",
        help_text="Укажите телеграм chat-id",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
    ]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = [
            "email",
            "phone_number",
            "citi",
        ]

    def __str__(self):
        return self.email
