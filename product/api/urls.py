from django.urls import path

from .views import ProductList, ProductDetail, OrderList, FinishedOrder, FooView

urlpatterns = [
    path('list', ProductList.as_view(), name='product-list'),
    path('list/<int:pk>', ProductDetail.as_view(), name='product-details'),
    path('orders', OrderList.as_view(), name='orders-list'),
    path('orders/finished', FinishedOrder.as_view(), name='finished-orders'),
    path('admin', FooView.as_view(), name='is-admin')
]
