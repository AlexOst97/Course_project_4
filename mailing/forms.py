from django import forms
from .models import Recipient, Message, Mailing, MailingAttempt

class RecipientForm(forms.ModelForm):
    class Meta:
        model = Recipient
        fields = ['email', 'full_name', 'comment',]


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['topic_message', 'content_message',]


class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ['status', 'message', 'recipient',]


class MailingAttemptForm(forms.ModelForm):
    class Meta:
        model = MailingAttempt
        fields = '__all__'


class ManagerMailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ['is_active',]