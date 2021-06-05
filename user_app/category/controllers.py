from rest_framework.response import Response
from service_objects.services import Service


class CreateCategoryService(Service):


    def process(self):
        data = self.data
        return Response({}, 200)
