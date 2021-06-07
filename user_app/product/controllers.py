from rest_framework.response import Response
from service_objects.services import Service

from user_app.models import Category, Product
from user_app.product.serializers import createProductSerializer, ListProductSerializer


class CreateProductService(Service):
    def process(self):
        product = Product.objects.create(
            name=self.data.get("data").get("name"),
            category=Category.objects.get(name=self.data.get("data").get("categoryName"),
                                          user_profile=self.data.get("user")),
        )
        return Response({"name": product.name}, 201)


class ListProductService(Service):
    def process(self):
        products = Product.objects.filter(category__user_profile=self.data.get("user"))
        return Response(ListProductSerializer(products, many=True).data, 200)
