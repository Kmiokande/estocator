from django.test import TestCase
from .models import Product


class ProductTestCase(TestCase):
    def setUp(self):
        print("[ Criando objetos produto ]")
        Product.objects.create(
            name="iBomb",
            brand="Mapple",
            price=7000.00,
            quantity=3,
            bar_code=12335879
        )
        Product.objects.create(
            name="Micro SD 16 GB",
            brand="São Disco",
            price=32.00,
            quantity=50,
            bar_code=1445789
        )

    def test_not_equal_bar_codes(self):
        print("[*] Testando se os códigos de barras são diferentes")
        i_bomb = Product.objects.get(bar_code=12335879)
        m_sd = Product.objects.get(bar_code=1445789)

        self.assertNotEquals(i_bomb, m_sd)
