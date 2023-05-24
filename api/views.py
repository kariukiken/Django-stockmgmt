from django.http import JsonResponse
from .models import Stock

def get_all_products(request):
    products = list(Stock.objects.values())
    return JsonResponse(products, safe=False)
