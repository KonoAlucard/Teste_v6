from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .views import signin, register, galeria

# register

class RegisterTestCase(TestCase):
    def test_valid_form_creates_user_and_redirects_to_login(self):
        
        response = self.client.post(reverse('register'), {
            'username': 'testando',
            'password1': 'clone205',
            'password2': 'clone205',
            'email': 'testando@gmail.com',
            'is_superuser': 1
        })
        
        
        self.assertRedirects(response, reverse('login'))

        
        user = authenticate(username='testando', password='clone205')
        self.assertIsNotNone(user)
        self.assertEqual(user.email, 'testando@gmail.com')


# login/signin

class SigninTestCase(TestCase):
    def test_authenticated_user_redirects_to_galeria(self):
        
        user = User.objects.create_user(username='testando', password='clone205')
        
        
        self.client.login(username='testando', password='clone205')
    
       
        response = self.client.get(reverse('login'))
        
      
        self.assertRedirects(response, reverse('galeria'))

    def test_get_request_returns_login_template(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'login.html')

    def test_valid_credentials_redirects_to_galeria(self):
        
        user = User.objects.create_user(username='testando', password='clone205')
        
        
        response = self.client.post(reverse('login'), {'username': 'testando', 'password1': 'clone205'})
        
        
        self.assertRedirects(response, reverse('galeria'))
        
        
        self.assertTrue(self.client.login(username='testando', password='clone205'))

    def test_invalid_credentials_returns_login_template(self):
        
        response = self.client.post(reverse('login'), {'username': 'testando', 'password1': 'senhaerrada'})
        
        
        self.assertTemplateUsed(response, 'login.html')

