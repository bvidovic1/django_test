from django.contrib import admin
from carsapp import models


class CarAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_filter = ['engine_type']
    search_fields = ['title', 'company']


admin.site.register(models.Car, CarAdmin)
