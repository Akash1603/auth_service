from rest_framework.response import Response
from service_objects.services import Service

from user_app.category.serializers import createCategorySerializer
from user_app.models import Category


class CreateCategoryService(Service):
    def process(self):
        category = Category.objects.create(
            name=self.data.get("data").get("name"),
            user_profile=self.data.get("user")
        )
        return Response({"name": category.name}, 201)


class ListCategoryService(Service):
    def process(self):
        categories = Category.objects.filter(user_profile=self.data.get("user"))
        return Response(createCategorySerializer(categories, many=True).data, 200)
