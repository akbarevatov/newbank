from django.db import models

# Create your models here.
class Card(models.Model):
    card_number = models.CharField(max_length=16, unique=True)
    cardholder_name = models.CharField(max_length=100)
    expiration_date = models.DateField()
    cvv = models.CharField(max_length=4)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cardholder_name} - {self.card_number}"