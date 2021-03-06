from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Campos Extras', {
          'fields' : (
              'is_premium',
              'is_artist',
               'fechaNacimiento',
               'pais',
               'foto',
          )  
        }),
    )

admin.site.register(User, UsuarioAdmin)