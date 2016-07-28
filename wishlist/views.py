from django.shortcuts import redirect
from django.views.generic.list import ListView
from .models import Wishlist
from products.models import Products
from django.core.exceptions import ObjectDoesNotExist
#from django.contrib.auth.decorators import login_required


class WishListView(ListView):
    template_name = 'wishlist.html'
    model = Wishlist
    context_object_name = 'wishlist'

    #   @login_required(redirect_field_name='home')
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('home')
        return super(WishListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(WishListView, self).get_context_data(**kwargs)
        user_id = self.request.user.id
        context['wishlist'] = Wishlist.objects.filter(user=user_id)
        return context


def wishlist_add_remove(request):
    if 'product_id' in request.POST:
        product_id = int(request.POST['product_id'])
    else:
        return redirect('wishlist')

    product = Products.objects.get(id=product_id)
    user_name = request.user

    if request.user.is_authenticated() and request.method == 'POST':
        try:
            wishlist = Wishlist.objects.get(product=product, user=user_name)
            wishlist.product.remove(product)
        except ObjectDoesNotExist:
            wishlist, created = Wishlist.objects.get_or_create(user=user_name)
            wishlist.product.add(product)

    return redirect(request.META.get('HTTP_REFERER', 'home'))
