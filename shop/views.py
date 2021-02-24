from django.shortcuts import render
from django.views import generic as views

from .models import Category, Product


class HomePageView(views.TemplateView):
    template_name = 'shop/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        context['categories'] = Category.objects.all()

        return context