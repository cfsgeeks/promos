from django.contrib import admin
from promos.models import Promo

class PromoAdmin(admin.ModelAdmin):
    list_display = ('title','url','publish_on','publish_until')

admin.site.register(Promo, PromoAdmin)
