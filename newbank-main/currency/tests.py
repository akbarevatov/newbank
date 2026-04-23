from django.test import TestCase
from .models import Currency    
from .views import exchange_api

# Create your tests here.
class CurrencyTests(TestCase):
    def test_currency_exchange(self):
        Currency.objects.create(name='US Dollar', code='USD', symbol='$', rate_to_usd=1.0)
        Currency.objects.create(name='Uzbekistan Som', code='UZS', symbol='UZS', rate_to_usd=12200.0)
        response = self.client.get('/currency/exchange_api/?from=USD&to=UZS&amount=100')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'result': 1220000.0})

    def test_from_currency_not_found(self):
        response = self.client.get('/currency/exchange_api/?to=USD&amount=100')
        self.assertEqual(response.status_code, 400)

    def test_amount_required(self):
        response = self.client.get('/currency/exchange_api/?from=USD&to=UZS')
        self.assertEqual(response.status_code, 400)

    def test_invalid_amount(self):
        response = self.client.get('/currency/exchange_api/?from=USD&to=UZS&amount=abc')
        self.assertEqual(response.status_code, 400)

    def test_negative_amount(self):
        response = self.client.get('/currency/exchange_api/?from=USD&to=UZS&amount=-100')
        self.assertEqual(response.status_code, 400)
        