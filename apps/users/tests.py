from django.test import TestCase
from models import *
import factory

class UserFactory(factory.Factory):
	FACTORY_FOR = Users

	first_name = factory.Sequence(lambda n: "Agent %03d" % n)
	last_name = 'Steve'
	email = factory.LazyAttribute(lambda obj: '%s@example.com' % obj.first_name)

	class UserTest(TestCase):
		user	=	factories.UserFactory.create()
        self.client.login(username=user.username, password='abc')
# Create your tests here.
