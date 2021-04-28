from django.test import TestCase
from django.urls import reverse
from .models import Maneger


# Create your tests here.

class ManagerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("Criando Objeto")
        Maneger.objects.create(name='higor', address = 'rua fulano de tal', birthday='2000-01-01', email='higor@gmail.com', cpf='21212')

    def test_name_of_name_create(self):
        print("Testando se o nome foi cadastrado em name")
        manager = Maneger.objects.get(id=1)
        expected_object_name = f'{manager.name}'
        self.assertEquals(expected_object_name, str(manager))

    def test_name_of_name_create_fail(self):
        print("Testando se o nome foi cadastrado em name Falha")
        manager = Maneger.objects.get(id=1)
        expected_object_name = f'{manager.name}'
        self.assertNotEquals(expected_object_name, 'HIGOR')

    def test_name_of_address_create(self):
        print("Testando se o endereço foi cadastrado em address")
        manager = Maneger.objects.get(id=1)
        expected_object_address = f'{manager.address}'
        self.assertEquals(expected_object_address, str(manager.address))

    def test_name_label(self):
        print("Testando Lable name")
        manager = Maneger.objects.get(id=1)
        field_label = manager._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_first_name_max_length(self):
        print("Testando tamanho do máximo endereço")
        manager = Maneger.objects.get(id=1)
        max_length = manager._meta.get_field('address').max_length
        self.assertEquals(max_length, 100)

class ManegerListViewTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

