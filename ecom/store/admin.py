from django.contrib import admin
from .models import *

@admin.register(Logins_emp)
class LoginAdmin(admin.ModelAdmin):
    list_display = (
        'username', 'first_name', 'last_name', 'email', 'phone', 'bio',
        'country', 'city_state', 'postal_code', 'tax_id'
    )
    search_fields = ('username', 'first_name', 'last_name', 'email')
    list_filter = ('country',)

@admin.register(HR_HR)
class HRAdmin(admin.ModelAdmin):
    list_display = (
        'username', 'first_name', 'last_name', 'email', 'phone', 'bio',
        'country', 'city_state', 'postal_code', 'tax_id'
    )
    search_fields = ('username', 'first_name', 'last_name', 'email')
    list_filter = ('country',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
   list_display = ('customer', 'order', 'sellings')