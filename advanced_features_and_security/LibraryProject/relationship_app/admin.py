from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Author)
admin.site.register(models.Book)
admin.site.register(models.Library)
admin.site.register(models.Librarian)


class CustomUserAdmin(UserAdmin):
    model = models.CustomUser
    
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'birth_date')})
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number', 'birth_date')})
    )
    

admin.site.register(models.CustomUser, CustomUserAdmin)