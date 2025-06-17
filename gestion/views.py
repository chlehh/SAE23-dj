from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

import json

def importer_application(request):
    message = ""
    if request.method == 'POST' and request.FILES.get('json_file'):
        try:
            # Lecture du fichier JSON
            fichier = request.FILES['json_file']
            data = json.load(fichier)

            # Création de l'application
            app_data = data['application']
            utilisateur = Utilisateur.objects.get(id=app_data['utilisateur_id'])
            application = Application.objects.create(
                nom=app_data['nom'],
                logo=app_data['logo'],
                utilisateur=utilisateur
            )

            # Création des services
            for service_data in data['services']:
                serveur = Serveur.objects.get(id=service_data['serveur_id'])
                Service.objects.create(
                    nom=service_data['nom'],
                    date_lancement=service_data['date_lancement'],
                    espace_memoire_utilise=service_data['espace_memoire_utilise'],
                    memoire_vive_necessaire=service_data['memoire_vive_necessaire'],
                    serveur=serveur
                )

            message = "Importation réussie."

        except Exception as e:
            message = f"Erreur : {e}"

    return render(request, 'gestion/import_application.html', {'message': message})



from django.shortcuts import render

def home(request):
    return render(request, 'gestion/home.html')


# === TypeServeur ===

def liste_type_serveur(request):
    types = TypeServeur.objects.all()
    return render(request, 'gestion/type_serveur/liste.html', {'types': types})

def ajouter_type_serveur(request):
    form = TypeServeurForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_type_serveur')
    return render(request, 'gestion/type_serveur/form.html', {'form': form})

def modifier_type_serveur(request, id):
    type_s = get_object_or_404(TypeServeur, id=id)
    form = TypeServeurForm(request.POST or None, instance=type_s)
    if form.is_valid():
        form.save()
        return redirect('liste_type_serveur')
    return render(request, 'gestion/type_serveur/form.html', {'form': form})

def supprimer_type_serveur(request, id):
    type_s = get_object_or_404(TypeServeur, id=id)
    type_s.delete()
    return redirect('liste_type_serveur')


# === Serveur ===
def liste_serveur(request):
    serveurs = Serveur.objects.all()
    return render(request, 'gestion/serveur/liste.html', {'serveurs': serveurs})

def ajouter_serveur(request):
    form = ServeurForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_serveur')
    return render(request, 'gestion/serveur/form.html', {'form': form})

def modifier_serveur(request, id):
    serveur = get_object_or_404(Serveur, id=id)
    form = ServeurForm(request.POST or None, instance=serveur)
    if form.is_valid():
        form.save()
        return redirect('liste_serveur')
    return render(request, 'gestion/serveur/form.html', {'form': form})

def supprimer_serveur(request, id):
    serveur = get_object_or_404(Serveur, id=id)
    serveur.delete()
    return redirect('liste_serveur')


# === Utilisateurs ===

def liste_utilisateur(request):
    utilisateurs = Utilisateur.objects.all()
    return render(request, 'gestion/utilisateur/liste.html', {'utilisateurs': utilisateurs})

def ajouter_utilisateur(request):
    form = UtilisateurForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_utilisateur')
    return render(request, 'gestion/utilisateur/form.html', {'form': form})

def modifier_utilisateur(request, id):
    utilisateur = get_object_or_404(Utilisateur, id=id)
    form = UtilisateurForm(request.POST or None, instance=utilisateur)
    if form.is_valid():
        form.save()
        return redirect('liste_utilisateur')
    return render(request, 'gestion/utilisateur/form.html', {'form': form})

def supprimer_utilisateur(request, id):
    utilisateur = get_object_or_404(Utilisateur, id=id)
    utilisateur.delete()
    return redirect('liste_utilisateur')


# === Service ===

def liste_service(request):
    services = Service.objects.all()
    return render(request, 'gestion/service/liste.html', {'services': services})

def ajouter_service(request):
    form = ServiceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_service')
    return render(request, 'gestion/service/form.html', {'form': form})

def modifier_service(request, id):
    service = get_object_or_404(Service, id=id)
    form = ServiceForm(request.POST or None, instance=service)
    if form.is_valid():
        form.save()
        return redirect('liste_service')
    return render(request, 'gestion/service/form.html', {'form': form})

def supprimer_service(request, id):
    service = get_object_or_404(Service, id=id)
    service.delete()
    return redirect('liste_service')


# === Application ===

def liste_application(request):
    applications = Application.objects.all()
    return render(request, 'gestion/application/liste.html', {'applications': applications})

def ajouter_application(request):
    form = ApplicationForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('liste_application')
    return render(request, 'gestion/application/form.html', {'form': form})

def modifier_application(request, id):
    application = get_object_or_404(Application, id=id)
    form = ApplicationForm(request.POST or None, request.FILES or None, instance=application)
    if form.is_valid():
        form.save()
        return redirect('liste_application')
    return render(request, 'gestion/application/form.html', {'form': form})

def supprimer_application(request, id):
    application = get_object_or_404(Application, id=id)
    application.delete()
    return redirect('liste_application')


# === Usage ===


def liste_usage(request):
    usages = Usage.objects.all()
    return render(request, 'gestion/usage/liste.html', {'usages': usages})

def ajouter_usage(request):
    form = UsageForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_usage')
    return render(request, 'gestion/usage/form.html', {'form': form})

def modifier_usage(request, id):
    usage = get_object_or_404(Usage, id=id)
    form = UsageForm(request.POST or None, instance=usage)
    if form.is_valid():
        form.save()
        return redirect('liste_usage')
    return render(request, 'gestion/usage/form.html', {'form': form})

def supprimer_usage(request, id):
    usage = get_object_or_404(Usage, id=id)
    usage.delete()
    return redirect('liste_usage')
