from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class RootRedirectTests(TestCase):
    def test_root_redirects_to_application_dashboard(self):
        response = self.client.get(reverse("home:root"))

        self.assertRedirects(
            response,
            reverse("home:dashboard"),
            fetch_redirect_response=False,
        )


class LoginViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="stockmanager",
            password="safe-test-password",
        )

    def test_login_page_renders(self):
        response = self.client.get(reverse("home:login"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/login.html")
        self.assertContains(response, "Welcome back")

    def test_valid_login_redirects_to_dashboard(self):
        response = self.client.post(
            reverse("home:login"),
            {"username": "stockmanager", "password": "safe-test-password"},
        )

        self.assertRedirects(response, reverse("home:dashboard"))
        self.assertEqual(int(self.client.session["_auth_user_id"]), self.user.pk)

    def test_dashboard_navigation_links_to_application_dashboard(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse("home:dashboard"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            f'href="{reverse("home:dashboard")}"',
        )
        self.assertNotContains(
            response,
            f'href="{reverse("admin:index")}"',
        )

    def test_invalid_login_shows_an_error(self):
        response = self.client.post(
            reverse("home:login"),
            {"username": "stockmanager", "password": "incorrect"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invalid username or password.")

    def test_external_next_url_is_not_followed(self):
        response = self.client.post(
            reverse("home:login"),
            {
                "username": "stockmanager",
                "password": "safe-test-password",
                "next": "https://example.com/phishing",
            },
        )

        self.assertRedirects(response, reverse("home:dashboard"))


class SignUpLoginFlowTests(TestCase):
    def test_newly_registered_user_can_log_in(self):
        signup_response = self.client.post(
            reverse("home:signup"),
            {
                "username": "newmanager",
                "email": "newmanager@example.com",
                "password": "safe-signup-password",
                "confirm_password": "safe-signup-password",
            },
        )

        self.assertRedirects(signup_response, reverse("home:login"))
        user = User.objects.get(username="newmanager")
        self.assertTrue(user.check_password("safe-signup-password"))

        login_response = self.client.post(
            reverse("home:login"),
            {"username": "newmanager", "password": "safe-signup-password"},
        )

        self.assertRedirects(login_response, reverse("home:dashboard"))
        self.assertEqual(int(self.client.session["_auth_user_id"]), user.pk)
