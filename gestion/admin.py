from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'utilisateur')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'serveur')

@admin.register(Serveur)
class ServeurAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'type_serveur')

@admin.register(Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'prenom', 'email')

@admin.register(TypeServeur)
class TypeServeurAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'description')

@admin.register(Usage)
class UsageAdmin(admin.ModelAdmin):
    list_display = ('id', 'application', 'service')
  