from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import User, Manager, Customer

# Register your models here.

@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    list_display = ('username', 'email' , 'first_name', 'last_name','contact','birth_date')

@admin.register(Manager)
class ManagerAdmin(ImportExportModelAdmin):
    list_display = ('user' , 'hotel')

@admin.register(Customer)
class CustomerAdmin(ImportExportModelAdmin):
    list_display = ('user',)
