from django.conf.urls import url
from .views import ProductsListView, ProductDetailView, CategoriesListView

urlpatterns = [
    url(r'^$', CategoriesListView.as_view(), name='categories'),
    url(r'^(?P<category>[a-z_-]+)/$', ProductsListView.as_view(), name='shop'),
    url(r'^(?P<category>[a-z_-]+)/page/(?P<page>\d+)/$', ProductsListView.as_view(), name='shop_page'),
    url(r'^(?P<category>[a-z_-]+)/(?P<slug>[a-z0-9_-]+)/$', ProductDetailView.as_view(), name='product_view'),
]

# urlpatterns = [
#     url(r'^/$', CategoriesListView.as_view(), name='categories'),
#     url(r'^(?P<category>[a-z_-]+)/', include(
#         url(r'^/$', ProductsListView.as_view(), name='shop'),
#         url(r'^/page/(?P<page>\d+)/$', ProductsListView.as_view(), name='shop_page'),
#         url(r'^/(?P<slug>[a-z0-9_-]+)/$', ProductDetailView.as_view(), name='product_view'),
#     )),
# ]