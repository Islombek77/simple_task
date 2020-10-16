import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from .models import Product


class ProductViewSetTestCase(APITestCase):

    def test_create_product(self):
        data = {
            'name': 'Macbook',
            'price': 2000
        }
        response = self.client.post('/api/products/list', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, 'Macbook')

    def test_get_product(self):
        data = {
            'name': 'Macbook',
            'price': 2000
        }
        self.client.post('/api/products/list', data, format='json')
        response = self.client.get('/api/products/list/1', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_product(self):
        data = {
            'name': 'Macbook',
            'price': 2000
        }
        self.client.post('/api/products/list', data, format='json')
        response = self.client.put('/api/products/list/1', {
            'name': 'Macbook Pro 2020',
            'price': 4200
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {
            'id': 1,
            'name': 'Macbook Pro 2020',
            'price': 4200
        })

    def test_get_product_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)



