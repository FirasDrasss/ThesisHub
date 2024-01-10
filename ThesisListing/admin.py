from django.contrib import admin
from .models import institutes,departments,thesis_listings
# Register your models here.


@admin.register(institutes)
class institutesAdmin(admin.ModelAdmin):
    pass


@admin.register(departments)
class departmentsAdmin(admin.ModelAdmin):
    pass
@admin.register(thesis_listings)
class thesis_listingsAdmin(admin.ModelAdmin):
    pass