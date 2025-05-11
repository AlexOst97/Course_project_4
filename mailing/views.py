from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from .models import Recipient, Message, Mailing
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .forms import RecipientForm, MessageForm, MailingForm
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


# МОДЕЛЬ Recipient
class RecipientCreateView(LoginRequiredMixin, CreateView):
    model = Recipient
    form_class  = RecipientForm
    template_name = 'recipient_create.html'
    success_url = reverse_lazy('mailing:recipient_list')


class RecipientUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipient
    form_class  = RecipientForm
    template_name = 'recipient_update.html'
    success_url = reverse_lazy('mailing:recipient_list')

    def get_change(self, request, *args, **kwargs):
        product = super().get_object()
        if product.owner == self.request.user:
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseForbidden("Вы не можете изменять этого получателя")


class RecipientDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipient
    template_name = 'recipient_delete.html'
    success_url = reverse_lazy('mailing:recipient_list')

    def get_change(self, request, *args, **kwargs):
        product = super().get_object()
        if product.owner == self.request.user:
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseForbidden("Вы не можете удалять этого получателя")


@method_decorator(cache_page(60 * 15), name='dispatch')
class RecipientListView(LoginRequiredMixin, ListView):
    model = Recipient
    template_name = 'recipient_list.html'
    context_object_name = 'recipients'


class RecipientDetailView(LoginRequiredMixin, DetailView):
    model = Recipient
    template_name = 'recipient_detail.html'
    context_object_name = 'recipient'


# МОДЕЛЬ Message
class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class  = MessageForm
    template_name = 'message_create.html'
    success_url = reverse_lazy('mailing:message_list')


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class  = MessageForm
    template_name = 'message_update.html'
    success_url = reverse_lazy('mailing:message_list')


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    template_name = 'message_delete.html'
    success_url = reverse_lazy('mailing:message_list')


@method_decorator(cache_page(60 * 15), name='dispatch')
class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'message_list.html'
    context_object_name = 'messages'


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    template_name = 'message_detail.html'
    context_object_name = 'message'


# МОДЕЛЬ Mailing
class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class  = MailingForm
    template_name = 'mailing_create.html'
    success_url = reverse_lazy('mailing:mailing_list')


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class  = MailingForm
    template_name = 'mailing_update.html'
    success_url = reverse_lazy('mailing:mailing_list')

    def get_change(self, request, *args, **kwargs):
        product = super().get_object()
        if product.owner == self.request.user:
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseForbidden("Вы не можете изменять эту рассылку")


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    template_name = 'mailing_delete.html'
    success_url = reverse_lazy('mailing:mailing_list')

    def get_change(self, request, *args, **kwargs):
        product = super().get_object()
        if product.owner == self.request.user:
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseForbidden("Вы не можете удалить эту рассылку")


@method_decorator(cache_page(60 * 15), name='dispatch')
class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing
    template_name = 'mailing_list.html'
    context_object_name = 'mailings'


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing
    template_name = 'mailing_detail.html'
    context_object_name = 'mailing'


@method_decorator(cache_page(60 * 15), name='dispatch')
class MailingTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_mailing"] = len(Mailing.objects.all())
        context["all_active_mailing"] = len(Mailing.objects.filter(status="Запущена"))
        context["all_recipient"] = len(Recipient.objects.all())
        return context
