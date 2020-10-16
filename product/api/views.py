from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from product.api.serializers import ProductSerializer, OrderSerializer
from product.models import Product, Order


class ProductList(APIView):

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        if (request.GET.get('sort_value')):
            products = Product.objects.filter(name__startswith=request.GET.get('sort_value'))
        else:
            products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderList(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


class FinishedOrder(APIView):
    def get(self, request):
        orders = Order.objects.filter(status='finish')
        price = 0
        quantity = 0
        for order in orders:
                price += order.product.price
                quantity += order.count
        return Response({'price': price, 'quantity': quantity})

from rest_framework.permissions import IsAdminUser


class FooView(APIView):

    permission_classes = [IsAdminUser]

    def get(self, request):
        return Response({"message": "HELLO ADMIN"})

    def post(self, request):
        return Response({"message": "HELLO ADMIN"})

    def put(self, request):
        return Response({"message": "HELLO ADMIN"})



