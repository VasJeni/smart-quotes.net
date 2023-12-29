from django.test import TestCase
from .models import Services

# Create your tests here.


class ServiceTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.service = Services.objects.create(
            title_en="test title eng",
            description_en="test eng text",
            title_uk="тестовий заголовок українською мовою",
            description_uk="Текстовий опис написаний ураїнською мовою",
        )

    def test_service_listing(self):
        self.assertEqual(f"{self.service.title_en}", "test title eng")
        self.assertEqual(f"{self.service.description_en}", "test eng text")
        self.assertEqual(
            f"{self.service.title_uk}", "тестовий заголовок українською мовою"
        )
        self.assertEqual(
            f"{self.service.description_uk}",
            "Текстовий опис написаний ураїнською мовою",
        )
