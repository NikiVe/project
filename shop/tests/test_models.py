from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from shop.models import Category, Product


class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name="django", slug="slug")

    def test_category_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), "django")


class TestProductsModel(TestCase):
    def setUp(self):
        Category.objects.create(name="django", slug="django")
        User.objects.create(username="admin")
        self.data1 = Product.objects.create(
            category_id=1,
            title="django beginners",
            created_by_id=1,
            slug="django-beginners",
            price="20.00",
            image="django",
        )
        # self.data2 = Product.products.create(
        #     category_id=1,
        #     title="django advanced",
        #     created_by_id=1,
        #     slug="django-advanced",
        #     price="20.00",
        #     image="django",
        #     is_active=False,
        # )

    def test_products_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), "django beginners")
