from django.test import TestCase
from models import User
import factory

class UserFactory(factory.Factory):
    class Meta:
        model = User

    first_name = 'Robert'
    last_name = 'Steve'
    email = 'selftest@example.com'
    password = 'password'


class UserTest(TestCase):
    
    user = UserFactory()

    def test_user_login_client(self):
        self.client.login(username=self.user.email, password=self.user.password)
    

    def test_get_full_name(self):
        full_name = self.user.get_full_name()
        if full_name == 'Robert Steve':
            return True
        else:
            return False

    def test_get_username(self):
        username = self.user.get_username()
        if username == 'selftest@example.com':
            return True
        else:
            return False
        
    def test_update_key(self):
        update_key = self.user.update_key()

        print update_key
        
