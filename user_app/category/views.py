from rest_framework.views import APIView
from oauth2_provider.contrib.rest_framework import (
    TokenMatchesOASRequirements,
    OAuth2Authentication,
)

from user_app.category.controllers import CreateCategoryService, ListCategoryService
from user_app.category.permissions import OnlyFirstNameAkashPermission
from user_app.category.serializers import createCategorySerializer


class CreateCategoryView(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenMatchesOASRequirements, OnlyFirstNameAkashPermission]
    required_alternate_scopes = {
        "POST": [["create"]],
        "GET": [["read"]]
    }

    @staticmethod
    def post(request):
        serial_data = createCategorySerializer(data=request.data)
        if serial_data.is_valid(raise_exception=True):
            return CreateCategoryService.execute(
                {"data": dict(serial_data.validated_data), "user": request.user}
            )

    @staticmethod
    def get(request):
        return ListCategoryService.execute({"user": request.user})
