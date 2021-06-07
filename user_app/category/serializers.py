from rest_framework import serializers


class createCategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
