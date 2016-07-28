from cart.models import Cart


def total(request):
    total_cost = 0
    total_quantity = 0
    for item in Cart.objects.filter(user=request.user.id):
        total_quantity += item.quantity
        total_cost += item.quantity * item.product.price

    return {'total_cost': total_cost,
            'total_quantity': total_quantity}
