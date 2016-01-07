from django.test import TestCase
from models import User
import factory

class UserFactory(factory.Factory):
    class Meta:
        model = User

    first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    last_name = 'Steve'
    email = factory.LazyAttribute(lambda obj: '%s@example.com' % obj.first_name)


class UserTest(TestCase):
    """
    Test Case for User factory
    """
    user = UserFactory()

    def test_user_login_client(self):
        self.client.login(username=self.user.email, password='abc')
