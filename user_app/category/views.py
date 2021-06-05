from rest_framework.views import APIView
from oauth2_provider.contrib.rest_framework import TokenMatchesOASRequirements, OAuth2Authentication

from user_app.category.controllers import CreateCategoryService
from user_app.category.permissions import OnlyFirstNameAkashPermission


class CreateCategoryView(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenMatchesOASRequirements, OnlyFirstNameAkashPermission]
    required_alternate_scopes = {
        "POST": [["create"]],
    }

    @staticmethod
    def post(request):
        return CreateCategoryService.execute({})
