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
        
    def test_get_short_name(self):
        short_name = self.user.get_short_name()
        if short_name == 'Robert Steve':
            return True
        else:
            return False
    
    def test_send_email(self):
        send_email = self.user.send_email(subject="Test subject", message="Test message")
        
    def test_send_templated_email(self):
        t_email = self.user.send_templated_email(template= "emails/welcome-email.html",context={'user': self},
            subject="subject")      
    
    def test_send_password_reset_email(self):
        p_email = self.user.send_password_reset_email()

