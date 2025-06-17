from gestion.models.utilisateur import Utilisateur
from gestion.models.type_serveur import TypeServeur
from gestion.models.serveur import Serveur

def run():
    utilisateur = Utilisateur.objects.create(nom="Amine", prenom="Zour", email="amine@example.com")
    print("Utilisateur ID:", utilisateur.id)

    type_srv = TypeServeur.objects.first()
    if not type_srv:
        type_srv = TypeServeur.objects.create(type="Web", description="Serveur Web générique")

    serveur = Serveur.objects.create(
        nom="ServeurTest",
        type_serveur=type_srv,
        nb_processeurs=8,
        capacite_memoire=32,
        capacite_stockage=512
    )
    print("Serveur ID:", serveur.id)
