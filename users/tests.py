#Django
from django.test import TestCase
from django.contrib.auth import get_user_model

class ClientTest(TestCase):
    """ Tests for the client model"""

    def test_new_superuser(self):
        """ Test new superuser is created correctly """
        db = get_user_model()
        super_user = db.objects.create_superuser(
            'test@super.com', 'test', 'test2', 'holamundo', '1065923143', 
        )
        self.assertEqual(super_user.email, 'test@super.com')
        self.assertEqual(super_user.first_name, 'test')
        self.assertEqual(super_user.last_name, 'test2')
        self.assertEqual(super_user.document, '1065923143')
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)
        self.assertEqual(str(super_user), 'test')
    
    def test_new_user(self):
        """  Test new user is created correctly  """
        db = get_user_model()
        user = db.objects.create_user(
            'test@super.com', 'test', 'test2', 'holamundo', '1065923143', 
        )
        self.assertEqual(user.email, 'test@super.com')
        self.assertEqual(user.first_name, 'test')
        self.assertEqual(user.last_name, 'test2')
        self.assertEqual(user.document, '1065923143')
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_active)