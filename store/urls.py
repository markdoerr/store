from django.conf.urls import url, include
from django.contrib import admin
from .views import HomeView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^shop/', include('products.urls')),
    url(r'^cart/', include('cart.urls')),
    url(r'^wishlist/', include('wishlist.urls')),
    url(r'^', include('loginsys.urls')),
]
