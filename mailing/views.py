from .models import Recipient, Message, Mailing
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import RecipientForm, MessageForm, MailingForm

# МОДЕЛЬ Recipient
class RecipientCreateView(CreateView):
    model = Recipient
    form_class  = RecipientForm
    template_name = 'recipient_create.html'
    success_url = reverse_lazy('mailing:recipient_list')


class RecipientUpdateView(UpdateView):
    model = Recipient
    form_class  = RecipientForm
    template_name = 'recipient_update.html'
    success_url = reverse_lazy('mailing:recipient_list')


class RecipientDeleteView(DeleteView):
    model = Recipient
    template_name = 'recipient_delete.html'
    success_url = reverse_lazy('mailing:recipient_list')


class RecipientListView(ListView):
    model = Recipient
    template_name = 'recipient_list.html'
    context_object_name = 'recipients'


class RecipientDetailView(DetailView):
    model = Recipient
    template_name = 'recipient_detail.html'
    context_object_name = 'recipient'


# МОДЕЛЬ Message
class MessageCreateView(CreateView):
    model = Message
    form_class  = MessageForm
    template_name = 'message_create.html'
    success_url = reverse_lazy('mailing:message_list')


class MessageUpdateView(UpdateView):
    model = Message
    form_class  = MessageForm
    template_name = 'message_update.html'
    success_url = reverse_lazy('mailing:message_list')


class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'message_delete.html'
    success_url = reverse_lazy('mailing:message_list')


class MessageListView(ListView):
    model = Message
    template_name = 'message_list.html'
    context_object_name = 'messages'


class MessageDetailView(DetailView):
    model = Message
    template_name = 'message_detail.html'
    context_object_name = 'message'


# МОДЕЛЬ Mailing
class MailingCreateView(CreateView):
    model = Mailing
    form_class  = MailingForm
    template_name = 'mailing_create.html'
    success_url = reverse_lazy('mailing:mailing_list')


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class  = MailingForm
    template_name = 'mailing_update.html'
    success_url = reverse_lazy('mailing:mailing_list')


class MailingDeleteView(DeleteView):
    model = Mailing
    template_name = 'mailing_delete.html'
    success_url = reverse_lazy('mailing:mailing_list')


class MailingListView(ListView):
    model = Mailing
    template_name = 'mailing_list.html'
    context_object_name = 'mailings'


class MailingDetailView(DetailView):
    model = Mailing
    template_name = 'mailing_detail.html'
    context_object_name = 'mailing'
