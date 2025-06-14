from django import forms
from .models import TypeServeur, Serveur, Utilisateur, Service, Application, Usage

class TypeServeurForm(forms.ModelForm):
    class Meta:
        model = TypeServeur
        fields = '__all__'

class ServeurForm(forms.ModelForm):
    class Meta:
        model = Serveur
        fields = '__all__'

class UtilisateurForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = '__all__'

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = '__all__'

class UsageForm(forms.ModelForm):
    class Meta:
        model = Usage
        fields = '__all__'
from django import forms
from .models import Service

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

    def clean(self):
        data = super().clean()
        memoire = data.get('memoire_vive_necessaire')
        serveur = data.get('serveur')

        if memoire and serveur:
            # Total de mémoire déjà utilisée sur ce serveur
            services_existants = Service.objects.filter(serveur=serveur)
            total_utilise = 0
            for s in services_existants:
                total_utilise += s.memoire_vive_necessaire

            disponible = serveur.capacite_memoire - total_utilise

            if memoire > disponible:
                raise forms.ValidationError(
                    f"Pas assez de mémoire sur le serveur. Il reste {disponible} Mo."
                )

        return data
