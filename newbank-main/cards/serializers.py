from rest_framework import serializers
from .models import Booking, Card

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'card_number', 'cardholder_name', 'expiration_date', 'cvv', 'balance']