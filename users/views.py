import secrets
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from users.forms import CustomUserCreationForm, UserUpdateForm, ManagerUserForm
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from django.shortcuts import get_object_or_404, redirect
from users.models import User
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView


class RegisterCreateView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        '''Переход на страницу пользователя после подтверждение почты'''
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email-confirm/{token}/"
        send_mail(
            subject="Подтверждение почты",
            message=f"Здравствуйте! Подтвердите почту {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)

    def email_verification(request, token):
        '''Сохранение пользователя'''
        user = get_object_or_404(User, token=token)
        user.is_active = True
        user.save()
        return redirect(reverse("users:login"))


class UserUpdateView(UpdateView, LoginRequiredMixin):
    model = User
    form_class = UserUpdateForm
    template_name = 'user_update.html'
    success_url = reverse_lazy('mailing:home')

    def get_change(self):
        return User.objects.filter(pk=self.request.user.pk)

    def get_form_class(self):
        user = self.request.user
        if user == user.has_perm("users.сan_block_users"):
            return ManagerUserForm
        return UserUpdateForm


class UserDeleteView(DeleteView, LoginRequiredMixin):
    model = User
    form_class = UserUpdateForm
    template_name = 'user_delete.html'
    success_url = reverse_lazy('mailing:home')

    def get_change(self):
        return User.objects.filter(pk=self.request.user.pk)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.filter(is_active = True)


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user'


class UserForgotPasswordView(SuccessMessageMixin, PasswordResetView):
    '''Сброс пароля через почту'''

    form_class = CustomUserCreationForm
    template_name = "password_reset.html.html"
    success_url = reverse_lazy("users:login")
    success_message = (
        "Письмо с инструкцией по восстановлению пароля отправлено на ваш email"
    )
    subject_template_name = "users/templates/email/password_subject_reset_mail.txt"
    email_template_name = "users/templates/email/password_reset_mail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Запрос на восстановление пароля"
        return context


class UserPasswordResetConfirmView(SuccessMessageMixin, PasswordResetConfirmView):
    '''Установка нового пароля'''

    form_class = CustomUserCreationForm
    template_name = "password_new.html.html"
    success_url = reverse_lazy("users:login")
    success_message = "Пароль успешно изменен"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Установить новый пароль"
        return context
