from django.http import JsonResponse
from .models import Class


def index(request):
    return JsonResponse(list(Class.objects.values()), safe=False)
