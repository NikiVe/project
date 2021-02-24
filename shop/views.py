from django.shortcuts import render
from django.views import generic as views

from .models import Category, Product


class HomePageView(views.ListView):
    model = Product
    template_name = 'shop/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        context['categories'] = Category.objects.all()

        return context


class ProductDetailView(views.DetailView):
    model = Product
    template_name = 'shop/products/detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = context[self.context_object_name]

        return context

class CategoryDetaillView(views.DetailView):
    model = Category
    template_name = 'shop/products/category.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = context[self.context_object_name]
         
        context['categories'] = Category.objects.all()
        # context['products'] = Product.objects.filter(category=category)
        context['products'] = category.product.all()

        return context