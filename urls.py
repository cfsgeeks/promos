from django.conf.urls import url
from promos.views import PromoList

urlpatterns = [
    url(r'^$', PromoList.as_view()),
    ]
