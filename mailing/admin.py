from django.contrib import admin
from mailing.models import Recipient, Message, Mailing, MailingAttempt


@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "full_name", "comment")
    list_filter = ("email", "full_name")
    search_fields = ("email", "full_name", "comment")


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("topic_message", "content_message")
    list_filter = ("topic_message",)
    search_fields = ("topic_message", "content_message")


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ("status", "message")
    list_filter = ("start_dispatch", "end_dispatch", "status")
    search_fields = ("start_dispatch", "end_dispatch", "status")


@admin.register(MailingAttempt)
class MailingAttemptAdmin(admin.ModelAdmin):
    list_display = ("start_attempt", "status", "answer_server", "mailing")
    list_filter = ("start_attempt", "status")
    search_fields = ("start_attempt", "status")
