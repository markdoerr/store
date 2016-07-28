from .models import Categories


def category(request):
    return {'category_footer': Categories.objects.all()}
