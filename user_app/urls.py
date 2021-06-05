from django.urls import path

from user_app.views import LoginView, RegistrationView

urlpatterns = [
    path("registration/", RegistrationView.as_view(), name="user_registration"),
    path("login/", LoginView.as_view(), name="user_login"),

]
