from django.core.management.base import BaseCommand
from mailing.models import Mailing, MailingAttempt
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from django.utils import timezone


class Command(BaseCommand):
    help = "Добавить рассылку в базу данных"

    def handle(self, *args, **options):
        mailings = Mailing.objects.filter(status__in=["created", "started"])

        for mailing in mailings:
            for recipient in mailing.recipient.all():
                try:
                    send_mail(
                        mailing.Message.topic_message,
                        mailing.Message.content_message,
                        from_email=EMAIL_HOST_USER,
                        recipient_list=[recipient.email],
                        fail_silently=False,
                    )
                    MailingAttempt.objects.create(
                        data=timezone.now(),
                        status=MailingAttempt.Successfully,
                        answer_server="Проверка связи",
                        mailing=mailing,
                    )
                    print("Рассылка успешно отправлена!")
                except Exception as error:
                    MailingAttempt.objects.create(
                        data=timezone.now(),
                        status=MailingAttempt.Not_successfully,
                        answer_server=f"{error}",
                        mailing=mailing,
                    )
                    print(f"{error}")
            mailing.save()
