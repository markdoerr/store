from django.conf.urls import url
from .views import CartView, cart_add, change_quantity, plus_minus, delete

urlpatterns = [
    url(r'^$', CartView.as_view(), name='cart'),
    url(r'^add$', cart_add, name='cart_add'),
    url(r'^change_quantity$', change_quantity, name='change_quantity'),
    url(r'^plus_minus$', plus_minus, name='plus_minus'),
    url(r'^delete$', delete, name='delete'),

]
