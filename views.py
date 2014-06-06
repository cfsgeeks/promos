from django.views.generic import DetailView,ListView
from promos.models import Promo
import datetime

TODAY = datetime.date.today()

class PromoList(ListView):
    queryset = Promo.objects.exclude(publish_until__lt=TODAY)
