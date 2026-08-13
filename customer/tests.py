from django.test import TestCase


class CustomerAPITests(TestCase):
    def test_create_customer_without_exposing_password(self):
        response = self.client.post(
            "/api/v1/customer/create",
            {
                "username": "api-customer",
                "email": "customer-api@example.com",
                "password": "secret-password",
            },
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertNotIn("password", response.json())
