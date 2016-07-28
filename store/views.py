from django.views.generic import TemplateView
#from products.models import Products

class HomeView(TemplateView):
    template_name = 'index.html'

    # def get_context_data(self, **kwargs):
    #   context = super(HomeView, self).get_context_data(**kwargs)
    #     user_id = self.request.user.id
    #     context['lasted_products'] = Products.objects.all
    #     return context