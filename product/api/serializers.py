from rest_framework import serializers
from product.models import Product, Order


class ProductSerializer(serializers.ModelSerializer):
    custom = serializers.SerializerMethodField('get_custom_field')

    def get_custom_field(self, product):
        return {"foo": "bar"}


    class Meta:
            model = Product
            fields = ["id", "name", "price", "custom"]



class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Order
        fields = "__all__"
