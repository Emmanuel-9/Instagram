from django.test import TestCase
from .models import Images,Profile

# Create your tests here.
class ImagesTest(TestCase):
    def setUp(self):
        self.image = Images(name='food',comments='Nice one',caption='Perfecto')