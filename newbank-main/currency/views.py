
from django.http import JsonResponse
from .models import Currency

def exchange_api(request):
    from_code = request.GET.get('from')
    to_code = request.GET.get('to')
    amount = request.GET.get('amount')

    if not from_code or not to_code:
        return JsonResponse({'error': 'Both currencies are required'}, status=400)

    if not amount:
        return JsonResponse({'error': 'Amount is required'}, status=400)

    try:
        amount = float(amount)
    except ValueError:
        return JsonResponse({'error': 'Invalid amount'}, status=400)

    from_currency = Currency.objects.filter(code=from_code).first()
    to_currency = Currency.objects.filter(code=to_code).first()

    if not from_currency or not to_currency:
        return JsonResponse({'error': 'Currency not found'}, status=400)

    if from_currency.rate_to_usd == 0:
        return JsonResponse({'error': 'Invalid source currency rate'}, status=400)

    amount_in_usd = amount / from_currency.rate_to_usd
    converted_amount = amount_in_usd * to_currency.rate_to_usd

    return JsonResponse({'result': converted_amount})
