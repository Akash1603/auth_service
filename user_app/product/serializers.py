from rest_framework import serializers

from user_app.category.serializers import createCategorySerializer


class createProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    categoryName = serializers.CharField(max_length=50)


class ListProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    categoryName = createCategorySerializer(source="category")
