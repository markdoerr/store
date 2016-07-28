from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, HttpResponse
from django.views.generic import TemplateView
from products.models import Products
from .models import Cart
from .context_processors import total
import json


class CartView(TemplateView):
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        user_id = self.request.user.id
        context['cart_products'] = Cart.objects.filter(user=user_id)

        return context


@csrf_exempt
def cart_add(request):
    if request.method == 'POST' and 'product_id' in request.POST:
        product_id = int(request.POST['product_id'])

        product = Products.objects.get(id=product_id)
        user_name = request.user

        if request.user.is_authenticated():
            cart, created = Cart.objects.get_or_create(user=user_name, product=product)
            # --option add another if product alrady in cart--
            # if created is False:
            #     cart.quantity += 1
            #     cart.save()
            cart_data = total(request)
            cart_data['total_cost'] = float(cart_data['total_cost'])
            return HttpResponse(json.dumps(cart_data))
    return HttpResponse('')


def change_quantity(request):
    response = redirect(request.META.get('HTTP_REFERER', 'home'))
    if 'product_id' in request.POST:
        product_id = int(request.POST['product_id'])
        quantity = request.POST[str(product_id)]
        if int(quantity) <= 0 or int(quantity) > 999:
            return response
    else:
        return response

    product = Products.objects.get(id=product_id)
    quantity = request.POST[str(product_id)]
    user_name = request.user

    if request.user.is_authenticated() and request.method == 'POST':
        cart = Cart.objects.get(user=user_name, product=product)
        cart.quantity = quantity
        cart.save()

    return response


def plus_minus(request):
    response = redirect(request.META.get('HTTP_REFERER', 'home'))
    if 'product_id' in request.POST:
        product_id = int(request.POST['product_id'])
        product = Products.objects.get(id=product_id)
        user_name = request.user

        if 'plus_minus' in request.POST and request.user.is_authenticated() and request.method == 'POST':
            cart = Cart.objects.get(user=user_name, product=product)
            value = request.POST['plus_minus']
            if value == '+':
                if cart.quantity != 999:
                    cart.quantity += 1
                    cart.save()
            elif value == '-':
                if cart.quantity != 1:
                    cart.quantity += -1
                    cart.save()

    return response


def delete(request):
    if 'item_id' in request.POST:
        item_id = int(request.POST['item_id'])
        user_name = request.user

        if request.user.is_authenticated() and request.method == 'POST':
            cart_item = Cart.objects.get(id=item_id, user=user_name)
            cart_item.delete()

    return redirect(request.META.get('HTTP_REFERER', 'home'))
