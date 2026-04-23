from django.db import models

# Create your models here.
class Currency(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    symbol = models.CharField(max_length=10)
    rate_to_usd = models.DecimalField(max_digits=20, decimal_places=6)  

    def __str__(self):
        return f"{self.name} ({self.code})"
