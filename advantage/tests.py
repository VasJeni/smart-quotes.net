from django.test import TestCase
from .models import Adventage

# Create your tests here.


class AdventageTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.advantage = Adventage.objects.create(
            title_en="Best offer",
            description_en="Good and cheap service",
            title_uk="Найкраща пропозиція",
            description_uk="Гарні та дешеві послуги",
        )

    def test_advantage_listing(self):
        self.assertEqual(f"{self.advantage.title_en}", "Best offer")
        self.assertEqual(f"{self.advantage.description_en}", "Good and cheap service")
        self.assertEqual(f"{self.advantage.title_uk}", "Найкраща пропозиція")
        self.assertEqual(f"{self.advantage.description_uk}", "Гарні та дешеві послуги")
