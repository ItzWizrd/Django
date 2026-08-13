from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from customer.models import Customer
from order.models import Order
from product.models import Product


class OrderCreateViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="order-manager",
            password="safe-test-password",
        )

    def test_create_page_uses_dedicated_template(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse("order:order-create"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "order/create_order.html")
        self.assertContains(response, "Create order")


class OrderListViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="order-manager",
            password="safe-test-password",
        )
        self.customer = Customer.objects.create(
            username="test-customer",
            email="customer@example.com",
            password="test-password",
        )
        for _ in range(11):
            Order.objects.create(customer=self.customer)
        self.client.force_login(self.user)

    def test_order_list_is_paginated_by_ten(self):
        response = self.client.get(reverse("order:order-list"))

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["is_paginated"])
        self.assertEqual(len(response.context["orders"]), 10)
        self.assertContains(response, "?page=2")

    def test_second_page_contains_remaining_order(self):
        response = self.client.get(reverse("order:order-list"), {"page": 2})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["orders"]), 1)
        self.assertEqual(response.context["page_obj"].number, 2)


class OrderCreateAPITests(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            username="api-customer",
            email="api-customer@example.com",
            password="test-password",
        )
        self.product = Product.objects.create(
            product_name="API product",
            price="10.00",
            quantity=1,
        )

    def test_create_order_without_trailing_slash(self):
        response = self.client.post(
            "/api/v1/create",
            {
                "customer": self.customer.pk,
                "status": Order.OrderStatus.PENDING,
                "order_details": [self.product.pk],
            },
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 201)
        order = Order.objects.get(pk=response.json()["order_id"])
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(list(order.order_details.all()), [self.product])

    def test_create_order_with_trailing_slash(self):
        response = self.client.post(
            "/api/v1/create/",
            {
                "customer": self.customer.pk,
                "status": Order.OrderStatus.PROCESSING,
                "order_details": [self.product.pk],
            },
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 201)

# Create your tests here.
