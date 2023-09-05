from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from django.http import JsonResponse
from rest_framework.response import Response
from .models import Promo
from .serializers import PromoSerializer
from datetime import date


@api_view()
@permission_classes((permissions.AllowAny,))
def promo_view(request):
    try:
        promo = Promo.objects.filter(promo__iexact=request.query_params.get('promo')).filter(is_active=True).filter(expiration__gte=date.today()).first()
    except:
        return JsonResponse({'error':'Неверный запрос'})
    serializer = PromoSerializer(promo)
    return Response(serializer.data)
