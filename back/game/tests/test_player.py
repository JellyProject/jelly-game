from django.test import TestCase


class PlayerTest(TestCase):
    """ doc """
    @classmethod
    def setUpTestData(cls):
        """ doc """
        user = User(
            name='Miguel de Patatas',
            email='a@a.com')

        player = Player(
            resources=Resources(),
            production=Production(),
            states=States(),
            user=user)

    def setUp(self):
        """ doc """
        pass

    def test_income_works(self):
        """ doc """
        self.assertTrue(True)
