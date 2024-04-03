from . import models
from django.views import generic


class ProductListView(generic.ListView):
    template_name = 'product/product_list.html'
    context_object_name = 'product'
    nodel = models.Product

    def get_queryset(self):
        return self.nodel.objects.filter().order_by('-id')


class FoodListView(generic.ListView):
    template_name = 'product/food_list.html'
    context_object_name = 'food'
    nodel = models.Product

    def get_queryset(self):
        return self.nodel.objects.filter(tags__name='food').order_by('-id')
