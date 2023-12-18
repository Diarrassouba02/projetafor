from djongo import models
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
import uuid




class Histoire(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_histories')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=False, related_name='created_histories')
    created_at = models.DateTimeField(auto_now_add=True)
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
    personne_trouve=models.CharField(max_length=900)
    groupement_trouve=models.CharField(max_length=900)
    accord_passe=models.CharField(max_length=200)
    lien=models.TextField(blank=True)
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
    chef_terre=models.CharField(max_length=50)
    mode_mise_a_diposition=models.CharField(max_length=200)
    groupement_liste=models.CharField(max_length=900)
    limite_litige_village=models.CharField(max_length=900)
    #fichier=models.ImageField(upload_to=fichier)
    complement=models.TextField()
    objects = models.DjongoManager()
