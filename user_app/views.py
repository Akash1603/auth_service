import requests
from django.contrib.auth import authenticate
from oauth2_provider.models import Application

from rest_framework.response import Response
from rest_framework.views import APIView

from user_app.models import UserProfile

# Create your views here.
from user_app.serializers import LoginSerializer, RegistrationSerializer


class RegistrationView(APIView):
    @staticmethod
    def post(request):
        serial_data = RegistrationSerializer(data=request.data)
        if serial_data.is_valid(raise_exception=True):
            user_data = dict(serial_data.validated_data)
            user_profile = UserProfile.objects.create(
                first_name=user_data["firstName"],
                last_name=user_data["lastName"],
                username=user_data["userName"],
                email=user_data["email"],
                mobile_no=user_data["mobileNo"],
                age=user_data["age"],
            )
            user_profile.set_password(user_data.get("password"))
            user_profile.save()
            Application.objects.create(
                user=user_profile,
                authorization_grant_type="password",
                client_type="confidential",
                name=user_profile.first_name,
            )
            return Response({"message": "User registered."}, status=201)


class LoginView(APIView):
    @staticmethod
    def post(request):
        try:
            serial_data = LoginSerializer(data=request.data)
            if serial_data.is_valid(raise_exception=True):
                user_data = dict(serial_data.validated_data)
                user = UserProfile.objects.get(username=user_data["userName"])
                validate_user = authenticate(
                    username=user_data["userName"], password=user_data["password"]
                )
                if validate_user is None:
                    return Response(
                        {"message": "invalid credential"},
                        status=400,
                    )
                app = Application.objects.filter(user=user)
                data = {
                    "username": user_data["userName"],
                    "password": user_data["password"],
                    "grant_type": "password",
                    "client_id": app.first().client_id,
                    "client_secret": app.first().client_secret,
                }
                token = requests.post("http://127.0.0.1:8000/" + "o/token/", data=data)
                token_data = {
                    "access_token": token.json().get("access_token"),
                    "expires_in": token.json().get("expires_in"),
                    "token_type": token.json().get("token_type"),
                }
                return Response(token_data, status=201)
        except UserProfile.DoesNotExist:
            return Response({"message": "User login failed."}, status=404)
