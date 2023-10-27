from django.shortcuts import render,redirect
from .models import Histoire
from django.contrib import messages

def index(request):
    histoire= Histoire.objects.all().count()
    contex={"histoire":histoire}
    return render(request, 'index.html')


# Forms
def formulairemanuscrit(request):
    if request.method=='POST':

        nom_region=request.POST.get('region')
        nom_departement=request.POST.get('departement')
        sous_prefecture=request.POST.get('sous_prefecture')
        nom_village=request.POST.get('village')
        nom_declarant=request.POST.get('nomdec')
        prenon_declarant=request.POST.get('prenomdec')
        qualite_declarant=request.POST.get('qualitedec')
        date_naissance_declarant=request.POST.get('datedec')
        lieu_naissance_declarant=request.POST.get('lieundec')
        lieu_residence_declarant=request.POST.get('lieudec')
        nom_fondateur=request.POST.get('nomf')
        prenom_fondateur=request.POST.get('prenomf')
        activite_fondateur=request.POST.get('activitef')
        origine_fondateur=request.POST.get('originef')
        lieu_inhimationf=request.POST.get('lieuinf')
        a=Histoire(nom_region=nom_region,nom_departement=nom_departement,
                 sous_prefecture=sous_prefecture,nom_village=nom_village,
                   nom_declarant=nom_declarant,prenon_declarant=prenon_declarant
                   ,qualite_declarant=qualite_declarant,date_naissance_declarant=date_naissance_declarant,
                   lieu_naissance_declarant=lieu_naissance_declarant,
                   lieu_residence_declarant=lieu_residence_declarant,
                   nom_fondateur=nom_fondateur,prenom_fondateur=prenom_fondateur,
                   origine_fondateur=origine_fondateur,activite_fondateur=activite_fondateur,
                   lieu_inhimationf=lieu_inhimationf)
        a.save()
        messages.success(request, 'Book was uploaded successfully')
        return redirect('index')
    else:
        messages.error(request, 'Book was not uploaded successfully')
        return render(request, 'forms/forms.html')

def  formulairetranscription(request):
    if request.method=='POST':
         nom_region=request.POST.get('region')
         nom_departement=request.POST.get('departement')
         sous_prefecture=request.POST.get('sous_prefecture')
         nom_village=request.POST.get('village')
         nom_declarant=request.POST.get('nomdec')
         prenon_declarant=request.POST.get('prenomdec')
         qualite_declarant=request.POST.get('qualitedec')
         date_naissance_declarant=request.POST.get('datedec')
         lieu_naissance_declarant=request.POST.get('lieundec')
         lieu_residence_declarant=request.POST.get('lieudec')
         nom_fondateur=request.POST.get('nomf')
         prenom_fondateur=request.POST.get('prenomf')
         activite_fondateur=request.POST.get('activitef')
         origine_fondateur=request.POST.get('originef')
         lieu_inhimationf=request.POST.get('lieuinf')
         a=Histoire(nom_region=nom_region,nom_departement=nom_departement,
                 sous_prefecture=sous_prefecture,nom_village=nom_village,
                   nom_declarant=nom_declarant,prenon_declarant=prenon_declarant
                   ,qualite_declarant=qualite_declarant,date_naissance_declarant=date_naissance_declarant,
                   lieu_naissance_declarant=lieu_naissance_declarant,
                   lieu_residence_declarant=lieu_residence_declarant,
                   nom_fondateur=nom_fondateur,prenom_fondateur=prenom_fondateur,
                   origine_fondateur=origine_fondateur,activite_fondateur=activite_fondateur,
                   lieu_inhimationf=lieu_inhimationf)
         a.save()
         messages.success(request, 'Book was uploaded successfully')
         return redirect('index')
    else:
         messages.error(request, 'Book was not uploaded successfully')
         return render(request,'forms/transcription/transcription.html')

