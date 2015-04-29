from django.contrib import admin
from .models import home




class homeAdmin(admin.ModelAdmin):
    list_display = ('tytul', 'data_publikacji', 'zdjecie')
    list_filter = ['data_publikacji']
    search_fields = ['tytul', 'opis']
    fieldsets = [
        (None,               {'fields': ['tytul']}),
        (None,               {'fields': ['opis']}),
        (None,               {'fields': ['nazwa_dzielnicy']}),
        (None,               {'fields': ['liczba_pokoi']}),
        (None,               {'fields': ['cena']}),
        (None,               {'fields': ['wspolrzedne_szer']}),
        (None,               {'fields': ['wspolrzedne_dl']}),
        (None,               {'fields': ['zdjecie']}),
        (None,               {'fields': ['data_publikacji']}),
    ]

admin.site.register(home, homeAdmin)

