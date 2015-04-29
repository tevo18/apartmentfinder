__author__ = 'madzik'
from django.contrib import admin
from .models import supermarket

class homeAdmin(admin.ModelAdmin):
    list_display = ('tytul', 'dzielnice', 'zdjecie')
    list_filter = ['dzielnice']
    search_fields = ['tytul', 'opis']
    fieldsets = [
    (None, {'fields': ['tytul']}),
    (None, {'fields': ['opis']}),
    (None, {'fields': ['nazwa_dzielnicy']}),
    (None, {'fields': ['wspolrzedne_szer']}),
    (None, {'fields': ['wspolrzedne_dl']}),
    (None, {'fields': ['zdjecie']}),
    ]
admin.site.register(supermarket, homeAdmin)