from django.contrib import admin
from .models import Home
from .models import Myhouse




class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date', 'photo')
    list_filter = ['publication_date']
    search_fields = ['title', 'description']
    fieldsets = [
        (None,               {'fields': ['title']}),
        (None,               {'fields': ['description']}),
        (None,               {'fields': ['district_name']}),
        (None,               {'fields': ['rooms_number']}),
        (None,               {'fields': ['price']}),
        (None,               {'fields': ['latitude']}),
        (None,               {'fields': ['longitude']}),
        (None,               {'fields': ['photo']}),
        (None,               {'fields': ['publication_date']}),
    ]




class MyhouseAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date', 'photo')
    list_filter = ['publication_date']
    search_fields = ['title', 'description']
    fieldsets = [
        (None,               {'fields': ['title']}),
        (None,               {'fields': ['description']}),
        (None,               {'fields': ['district_name']}),
        (None,               {'fields': ['rooms_number']}),
        (None,               {'fields': ['price']}),
        (None,               {'fields': ['latitude']}),
        (None,               {'fields': ['longitude']}),
        (None,               {'fields': ['photo']}),
        (None,               {'fields': ['publication_date']}),
    ]
admin.site.register(Home, HomeAdmin)
admin.site.register(Myhouse, MyhouseAdmin)
