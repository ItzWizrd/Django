from django.test import TestCase


class SupplierAPITests(TestCase):
    def test_create_supplier(self):
        response = self.client.post(
            "/api/v1/suppliers/create",
            {
                "name": "API supplier",
                "email": "supplier-api@example.com",
                "is_active": True,
            },
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["name"], "API supplier")
