from django.views.generic import ListView
from promos.models import Promo
import datetime

TODAY = datetime.date.today()

class PromoList(ListView):
    queryset = Promo.objects.filter(status__exact=2).exclude(publish_until__lt=TODAY).order_by('-publish_on')
