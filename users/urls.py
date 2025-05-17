from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import (RegisterCreateView,
                         UserForgotPasswordView,
                         UserPasswordResetConfirmView,
                         UserUpdateView,
                         UserDeleteView,
                         UserListView,
                         UserDetailView)

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='users:login'), name='logout'),
    path('register/', RegisterCreateView.as_view(), name='register'),
    path("password_reset/", UserForgotPasswordView.as_view(), name="password_reset"),
    path("set_new_password/<uidb64>/<token>/", UserPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
]