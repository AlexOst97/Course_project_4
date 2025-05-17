from django.db import models
from users.models import User


class Recipient(models.Model):
    "Клаcc, получатель рассылки"

    email = models.EmailField(unique=True, verbose_name="Email")
    full_name = models.CharField(max_length=200, verbose_name="ФИО")
    comment = models.TextField(blank=True, null=True, verbose_name="Комментарий")
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="user_recipient",
        verbose_name="Владелец",
    )

    class Meta:
        verbose_name = "Получатель"
        verbose_name_plural = "Получатели"
        ordering = [
            "email",
            "full_name",
        ]

    def __str__(self):
        return f"{self.full_name} - {self.email}"


class Message(models.Model):
    "Класс, сообщение"

    topic_message = models.CharField(max_length=200, verbose_name="Тема сообщения")
    content_message = models.TextField(
        blank=True, null=True, verbose_name="Тело сообщения"
    )

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = [
            "topic_message",
        ]

    def __str__(self):
        return f"{self.topic_message}"


class Mailing(models.Model):
    """Класс, рассылка"""

    start_dispatch = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата и время первой отправки"
    )
    end_dispatch = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата и время окончания отправки"
    )

    Created = "Создана"
    Launched = "Запущена"
    Completed = "Завершена"

    STATUS_CHOICES = [
        (Created, "Создана"),
        (Launched, "Запущена"),
        (Completed, "Завершена"),
    ]

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="Created",
        verbose_name="Статус рассылки",
    )
    message = models.ForeignKey(
        Message, on_delete=models.CASCADE, verbose_name="Сообщение"
    )
    recipient = models.ManyToManyField(Recipient, verbose_name="Получатель")
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="user_mailing",
        verbose_name="Владелец",
    )
    is_active = models.BooleanField(default=True, verbose_name="Признак публикации")

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        ordering = [
            "start_dispatch",
            "end_dispatch",
            "status",
        ]
        permissions = [
            ("can_disable_mailing", "Может отключать рассылки"),
        ]

    def __str__(self):
        return f"{self.id}"


class MailingAttempt(models.Model):
    "Класс, попытка рассылки"

    start_attempt = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата и время попытки"
    )

    Successfully = "Успешно"
    Not_successfully = "Не успешно"

    STATUS_CHOICES = [
        (Successfully, "Успешно"),
        (Not_successfully, "Не успешно"),
    ]

    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, verbose_name="Статус рассылки"
    )
    answer_server = models.TextField(verbose_name="Ответ почтового сервера")
    mailing = models.ForeignKey(
        Mailing, on_delete=models.CASCADE, verbose_name="Рассылка"
    )

    class Meta:
        verbose_name = "Попытка рассылки"
        verbose_name_plural = "Попытки рассылок"
        ordering = [
            "start_attempt",
            "status",
        ]

    def __str__(self):
        return f"{self.id}"
