from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    avatar = models.ImageField(
        upload_to="users/image", blank=True, null=True, verbose_name="Изображение"
    )
    phone_number = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Номер телефона"
    )
    country = models.CharField(
        max_length=50, null=True, blank=True, verbose_name="Страна"
    )
    token = models.CharField(
        max_length=100, verbose_name="token", blank=True, null=True
    )
    is_active = models.BooleanField(default=True, verbose_name="Активный пользователь")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        permissions = [
            ("сan_block_users", "Может блокировать пользователей"),
        ]

    def __str__(self):
        return f"{self.email}"
