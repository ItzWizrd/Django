from django.test import TestCase

from user.models import Role, User


class UserAPITests(TestCase):
    def test_create_and_retrieve_user_without_exposing_password(self):
        role = Role.objects.create(name="Manager")

        create_response = self.client.post(
            "/api/v1/user/create",
            {
                "username": "api-user",
                "email": "api-user@example.com",
                "password": "secret-password",
                "role": role.pk,
            },
            content_type="application/json",
        )

        self.assertEqual(create_response.status_code, 201)
        self.assertNotIn("password", create_response.json())
        user = User.objects.get(email="api-user@example.com")

        detail_response = self.client.get(
            f"/api/v1/user/edit-delete-get-user/{user.pk}/"
        )
        self.assertEqual(detail_response.status_code, 200)
        self.assertNotIn("password", detail_response.json())

    def test_create_role(self):
        response = self.client.post(
            "/api/v1/user/roles/create/",
            {"name": "Operator"},
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 201)
