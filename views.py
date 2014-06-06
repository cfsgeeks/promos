from django.views.generic import ListView
from promos.models import Promo
import datetime

TODAY = datetime.date.today()

class PromoList(ListView):
    queryset = Promo.objects.filter(publish_until__gte=TODAY,status__exact=2)
