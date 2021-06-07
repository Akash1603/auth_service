from rest_framework.response import Response
from service_objects.services import Service

from user_app.models import Category, UserProfile


class CreateCategoryService(Service):
    def process(self):
        category = Category.objects.create(
            name=self.data.get("data").get("name"),
            user_profile=UserProfile.objects.get(id=self.data.get("user").id),
        )
        return Response({"name": category.name}, 201)
