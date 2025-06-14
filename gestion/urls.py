from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # TypeServeur
    path('types/', views.liste_type_serveur, name='liste_type_serveur'),
    path('types/ajouter/', views.ajouter_type_serveur, name='ajouter_type_serveur'),
    path('types/modifier/<int:id>/', views.modifier_type_serveur, name='modifier_type_serveur'),
    path('types/supprimer/<int:id>/', views.supprimer_type_serveur, name='supprimer_type_serveur'),

    # Serveur
    path('serveurs/', views.liste_serveur, name='liste_serveur'),
    path('serveurs/ajouter/', views.ajouter_serveur, name='ajouter_serveur'),
    path('serveurs/modifier/<int:id>/', views.modifier_serveur, name='modifier_serveur'),
    path('serveurs/supprimer/<int:id>/', views.supprimer_serveur, name='supprimer_serveur'),

    # Utilisateur
    path('utilisateurs/', views.liste_utilisateur, name='liste_utilisateur'),
    path('utilisateurs/ajouter/', views.ajouter_utilisateur, name='ajouter_utilisateur'),
    path('utilisateurs/modifier/<int:id>/', views.modifier_utilisateur, name='modifier_utilisateur'),
    path('utilisateurs/supprimer/<int:id>/', views.supprimer_utilisateur, name='supprimer_utilisateur'),

    # Service
    path('services/', views.liste_service, name='liste_service'),
    path('services/ajouter/', views.ajouter_service, name='ajouter_service'),
    path('services/modifier/<int:id>/', views.modifier_service, name='modifier_service'),
    path('services/supprimer/<int:id>/', views.supprimer_service, name='supprimer_service'),

    # Application
    path('applications/', views.liste_application, name='liste_application'),
    path('applications/ajouter/', views.ajouter_application, name='ajouter_application'),
    path('applications/modifier/<int:id>/', views.modifier_application, name='modifier_application'),
    path('applications/supprimer/<int:id>/', views.supprimer_application, name='supprimer_application'),

    # Usage
    path('usages/', views.liste_usage, name='liste_usage'),
    path('usages/ajouter/', views.ajouter_usage, name='ajouter_usage'),
    path('usages/modifier/<int:id>/', views.modifier_usage, name='modifier_usage'),
    path('usages/supprimer/<int:id>/', views.supprimer_usage, name='supprimer_usage'),
]
