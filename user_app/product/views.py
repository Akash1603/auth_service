from rest_framework.views import APIView
from oauth2_provider.contrib.rest_framework import (
    TokenMatchesOASRequirements,
    OAuth2Authentication,
)

from user_app.category.permissions import OnlyFirstNameAkashPermission
from user_app.product.controllers import CreateProductService, ListProductService
from user_app.product.serializers import createProductSerializer


class CreateProductView(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenMatchesOASRequirements, OnlyFirstNameAkashPermission]
    required_alternate_scopes = {
        "POST": [["create"]],
        "GET": [["read"]]
    }

    @staticmethod
    def post(request):
        serial_data = createProductSerializer(data=request.data)
        if serial_data.is_valid(raise_exception=True):
            return CreateProductService.execute(
                {"data": dict(serial_data.validated_data), "user": request.user}
            )

    @staticmethod
    def get(request):
        return ListProductService.execute({"user": request.user})
