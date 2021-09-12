from django.contrib import admin

from quickstart.models import Order


@admin.register(Order)
class OrderAdminConfig(admin.ModelAdmin):

    FIELDS = ('customer', 'email', 'description')

    search_fields = FIELDS
    list_display = FIELDS
    list_filter = ('email',)
