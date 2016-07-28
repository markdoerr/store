from django.conf.urls import url
from .views import WishListView, wishlist_add_remove


urlpatterns = [
    url(r'^$', WishListView.as_view(), name='wishlist'),
    url(r'^add/$', wishlist_add_remove, name='wishlist_add_remove'),
]
