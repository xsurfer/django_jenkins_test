from django.test import TestCase

# Create your tests here.
from .models import Animal


class AnimalTestCase(TestCase):
    def setUp(self):
        pass
        # Animal.objects.create(animal="lion", salutation="roar")
        # Animal.objects.create(animal="cat", salutation="meow")

    def test_fail(self):
        """
        fail_test() should always fail
        """
        self.assertEqual(False, False)

    def test_success(self):
        """
        success_test() should always succeed
        """
        self.assertEqual(True, True)

    # def test_animals_can_speak(self):
    #     """Animals that can speak are correctly identified"""
    #     lion = Animal.objects.get(animal="lion")
    #     cat = Animal.objects.get(animal="cat")
    #     self.assertEqual(lion.speak(), 'The lion says "roar"')
    #     self.assertEqual(cat.speak(), 'The cat says "meow"')