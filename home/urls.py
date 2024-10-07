from django.urls import path
from .views import home_view, contact_view
from .views import order_product, order_success

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),  # Add contact page URL
     path('order/<int:product_id>/', order_product, name='order_product'),
     path('order/success/', order_success, name='order_success'),
]
