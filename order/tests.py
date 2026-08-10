from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


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

# Create your tests here.
