from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("login/", views.login_request, name='login'),
    path("register/post-handle/", views.post_handle, name="post_handle"),
    path("register/", views.register_request, name='register'),
    path("auth", views.handle_login, name="handle_login"),
    path("home/", views.home, name="home"),
    path("api/mongo-data/", views.mongodb_data, name="MongoDB Data"),
    path("email", views.welcome_mail, name="welcome_mail"),
    path("pypy", views.pypy, name="pypy"),
    path("success_login", views.success_login, name="success_login"),
    path("success_registration", views.success_registration, name="success_registration"),
    path("success_pass_reset", views.execute_pass_reset, name="success_pass_reset"),
    path("forgot-password/", views.forgot_password, name="forgot-password"),
    path("reset-password/", views.reset_password, name="reset-password"),
    path("verify-user/", views.validate_forgot_password, name="verify-user"),
    path("sign-out/", views.sign_out, name="sign-out"),
    path("execute_pass_reset", views.execute_pass_reset, name="execute_pass_reset"),
    path("user_profile", views.user_profile, name="user_profile")
]