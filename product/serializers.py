from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    custom = serializers.SerializerMethodField('get_custom_obj')

    class Meta:
        model = Product
        fields = ["id", "name", "price", "custom"]





