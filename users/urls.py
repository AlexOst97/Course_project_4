from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import RegisterView, UserForgotPasswordView, UserPasswordResetConfirmView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='mailing:home'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path("password_reset/", UserForgotPasswordView.as_view(), name="password_reset"),
    path("set_new_password/<uidb64>/<token>/", UserPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
]