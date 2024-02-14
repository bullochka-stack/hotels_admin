from django.contrib import admin

from hotels.models import City, Hotel


admin.site.site_header = 'Hotels Admin Panel'


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    pass
