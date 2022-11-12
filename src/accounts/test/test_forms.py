from accounts.forms import UserRegisterFrom

from django.test import TestCase


class TestForms(TestCase):
    def setUp(self):
        self.username = 'user_1'
        self.password = 'qwerty1234'
        self.email = 'user_1@test.com'

    def test_register_form_valid_data(self):
        form = UserRegisterFrom(
            data={
                'username': self.username,
                'email': self.email,
                'password1': self.password,
                'password2': self.password
            }
        )
        self.assertTrue(form.is_valid())

    def test_register_form_no_data(self):
        form = UserRegisterFrom(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)
