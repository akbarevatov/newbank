from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

supported_cards = [
    "Uzcard",
    "Humo",
    "Visa",
    "MasterCard",
    "UnionPay",
    "Mir",
]

# Create your views here.
def index(request):
    return render(request, 'cards/index.html', {'cards': supported_cards})

def card_info(request, card_name):
    return HttpResponse(f'Open {card_name} card at NewBank!')
