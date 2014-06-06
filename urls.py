from django.conf.urls import url
from promos.views import PromoList

urlpatterns = [
    url(r'^$', JobList.as_view()),
    ]
