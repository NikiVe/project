from django.urls import path

from . views import HomePageView, ProductDetailView, CategoryDetaillView

app_name = 'shop'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('search/<slug:slug>/', CategoryDetaillView.as_view(), name='category_list'),

]
