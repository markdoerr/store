from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Products, Categories
from wishlist.models import Wishlist
from cart.models import Cart


class ProductsListView(ListView):
    template_name = 'shop.html'
    model = Products
    context_object_name = 'products'
    paginate_by = 8
    paginate_orphans = 1

    def get_queryset(self):
        cur_queryset = super(ProductsListView, self).get_queryset()
        category = Categories.objects.get(slug=self.kwargs['category'])
        queryset = cur_queryset.filter(visible=1, category_id=category.id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)
        context['category_slug'] = Categories.objects.get(slug=self.kwargs['category']).slug

        for product in context['products']:
                        product.is_in_cart = Cart.objects.filter(product=product,
                                                           user=self.request.user).exists()

        return context


class CategoriesListView(ListView):
    template_name = 'categories.html'
    model = Categories
    context_object_name = 'categories'


class ProductDetailView(DetailView):
    template_name = 'product.html'
    model = Products
    context_object_name = 'product'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        product_id = context['product'].id
        category_id = context['product'].category_id

        context['products'] = Products.objects.filter(visible=1, category_id=category_id).exclude(id=product_id)[:5]
        context['category_slug'] = Categories.objects.get(id=category_id).slug

        product_tag_list = []
        for product_tag in context['product'].tag.all():
            product_tag_list.append(product_tag.id)

        category_accessories_id = 8
        context['accessories'] = Products.objects.filter(visible=1,
                                                         category_id=category_accessories_id,
                                                         tag__in=product_tag_list).exclude(id=product_id).distinct()

        if self.request.user.is_authenticated():
            context['wishlist_product'] = Wishlist.objects.filter(product=context['product'],
                                                                  user=self.request.user).exists()
            # not working without autorzation!
            context['cart_object'] = Cart.objects.filter(product=context['product'],
                                                                  user=self.request.user).exists()
            for accessuar in context['accessories']:
                accessuar.is_in_cart = Cart.objects.filter(product=accessuar,
                                                           user=self.request.user).exists()

        return context

    def get_queryset(self):
        cur_queryset = super(ProductDetailView, self).get_queryset()
        queryset = cur_queryset.filter(visible=1, category__slug=self.kwargs['category'])
        return queryset
