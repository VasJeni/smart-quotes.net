from django.test import TestCase
from django.utils import translation
from django.urls import reverse, resolve

from .views import HomePageView

# Create your tests here.


class HomepageTest(TestCase):
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_url_exist_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, "home.html")

    def test_hompage_contains_correcr_html(self):
        self.assertContains(self.response, "Smart Quotes")

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Hi, there! I should not be on the page.")

    def test_homepage_url_resolves_homepagaview(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)

    # translations
    # have to create bd for translate tests
    def test_homepage_in_english(self):
        translation.activate("en")  # Activate en language
        response = self.client.get(reverse("home"))
        # self.assertContains(response, '<html lang="en">')
        self.assertContains(
            response, "WE HELP TECHNOLOGIES COMPANIES TO HIRE HIGH-PERFORMANCE TEAMS."
        )

    def test_homepage_in_ukrainian(self):
        translation.activate("uk")  # # Activate ukranian
        response = self.client.get(reverse("home"))
        # self.assertContains(response, '<html lang="uk">')
        self.assertContains(
            response,
            "МИ ДОПОМАГАЄМО ТЕХНОЛОГІЧНИМ КОМПАНІЯМ НАЙМАТИ ВИСОКОЕФЕКТИВНІ КОМАНДИ.",
        )
