from django.test import TestCase


class ProductAPITests(TestCase):
    def test_create_product(self):
        response = self.client.post(
            "/api/v1/product/create/",
            {
                "product_name": "API product",
                "price": "24.99",
                "quantity": 4,
            },
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["product_name"], "API product")

    def test_create_category(self):
        response = self.client.post(
            "/api/v1/product/categories/create",
            {"category_name": "API category"},
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 201)
