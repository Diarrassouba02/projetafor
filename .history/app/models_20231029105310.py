from djongo import models
from django import forms
from django.core.exceptions import ValidationError





class MyPairListField(models.Field):
    description = "Custom list field that stores a list of pairs (lists of two elements)"

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 255  # Vous pouvez ajuster la longueur maximale au besoin
        super(MyPairListField, self).__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        if value is None:
            return []
        # Convertit la chaîne de base de données en une liste de listes
        return [pair.strip().strip('[]').split(',') for pair in value.split(';')]

    def to_python(self, value):
        if isinstance(value, list):
            return value
        if value is None:
            return []
        # Convertit la chaîne Python en une liste de listes
        return [pair.strip().strip('[]').split(',') for pair in value.split(';')]

    def get_prep_value(self, value):
        if isinstance(value, list):
            # Convertit la liste de listes en une chaîne pour la base de données
            return ';'.join([','.join(pair) for pair in value])
        return value

    def formfield(self, **kwargs):
        defaults = {
            'max_length': self.max_length,
            'widget': forms.TextInput(attrs={'class': 'my-custom-pair-list-input'}),
        }
        defaults.update(kwargs)
        return super(MyPairListField, self).formfield(**defaults)







class MyListField(models.Field): #ma propre liste fields
    description = "python list"

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 255
        super(MyListField, self).__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        if value is None:
            return []
        return [item.strip() for item in value.split(',')]

    def to_python(self, value):
        if isinstance(value, list):
            return value
        if value is None:
            return []
        return [item.strip() for item in value.split(',')]

    def get_prep_value(self, value):
        if isinstance(value, list):
            return ', '.join(value)
        return value

    def formfield(self, **kwargs):
        defaults = {
            'max_length': self.max_length,
            'widget': forms.TextInput(attrs={'class': 'my-custom-list-input'}),
        }
        defaults.update(kwargs)
        return super(MyListField, self).formfield(**defaults)


class Histoire(models.Model):
    id = models.ObjectIdField()
    nom_region=models.CharField(max_length=2000)
    nom_departement=models.CharField(max_length=200)
    sous_prefecture=models.CharField(max_length=200)
    nomenq=models.CharField(max_length=200)
    prenomenq=models.CharField(max_length=200)
    nom_village=models.CharField(max_length=200)
    signification=models.TextField()
    nom_declarant=models.CharField(max_length=200)
    prenon_declarant=models.CharField(max_length=200)
    qualite_declarant=models.CharField(max_length=200)
    date_naissance_declarant=models.DateField()
    lieu_naissance_declarant=models.CharField(max_length=200)
    lieu_residence_declarant=models.CharField(max_length=200)
    nom_fondateur=models.CharField(max_length=200)
    prenom_fondateur=models.CharField(max_length=200)
    activite_fondateur=models.CharField(blank=True,max_length=200)
    lieu_inhimationf=models.CharField(max_length=200)
    origine_fondateur=models.CharField(max_length=200)
    personne_trouve=models.CharField(max_length=200)
    accord_passe=models.CharField(max_length=200)
    lien=models.TextField()
    epoque_installation=models.TextField()
    succeseur_nom_prenon_date=models.CharField(max_length=900)
    nomlignage=models.CharField(max_length=900)
    dateoff=models.CharField(max_length=200)
    autoriteoff=models.CharField(max_length=200)
    acte_creation=models.CharField(max_length=200)
    campement_nom_origine=models.CharField(max_length=900)
    site_adoration=models.CharField(max_length=900)
    ancien_site=models.CharField(max_length=900)
    mode_accès_terre=models.TextField()
    #mode_mise_a_diposition=models.CharField(max_length=200)


    #chef_terreter=models.BooleanField()

    #groupement_liste=MyListField()
    #list_village_voisin=MyListField()
    #état_litige=models.BooleanField()
    #limite_ouest=models.CharField(max_length=200)
    #limite_nord=models.CharField(max_length=200)
    #limite_sud=models.CharField(max_length=200)
    #limite_est=models.CharField(max_length=200)
    #libellé_litige=models.TextField()
    #complement=models.TextField()
    objects = models.DjongoManager()
