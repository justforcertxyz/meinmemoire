from django.test import TestCase
from .models import Memoire, BasePlanMemoire, PremiumPlanMemoire
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()


class MemoireModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="Foo", password="bar")
        self.memoire_type = Memoire

    def test_model_exists(self):
        self.assertTrue(issubclass(self.memoire_type, Memoire))

        count = self.memoire_type.objects.count()
        self.assertEqual(count, 0)

    def test_create(self):
        memoire = self.memoire_type.create(user=self.user)
        self.assertTrue(isinstance(memoire, Memoire))

        count = self.memoire_type.objects.count()
        self.assertEqual(count, 1)

        self.assertEqual(memoire.user, self.user)


class BasePlanMemoireModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="Foo", password="bar")
        self.memoire_type = BasePlanMemoire

    def test_model_exists(self):
        self.assertTrue(issubclass(self.memoire_type, Memoire))

        count = self.memoire_type.objects.count()
        self.assertEqual(count, 0)

    def test_create(self):
        memoire = self.memoire_type.create(user=self.user)
        self.assertTrue(isinstance(memoire, BasePlanMemoire))

        count = self.memoire_type.objects.count()
        self.assertEqual(count, 1)

        self.assertEqual(memoire.user, self.user)


class PremiumPlanMemoireModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="Foo", password="bar")
        self.memoire_type = PremiumPlanMemoire

    def test_model_exists(self):
        self.assertTrue(issubclass(self.memoire_type, Memoire))

        count = self.memoire_type.objects.count()
        self.assertEqual(count, 0)

    def test_create(self):
        memoire = self.memoire_type.create(user=self.user)
        self.assertTrue(isinstance(memoire, PremiumPlanMemoire))

        count = self.memoire_type.objects.count()
        self.assertEqual(count, 1)

        self.assertEqual(memoire.user, self.user)
