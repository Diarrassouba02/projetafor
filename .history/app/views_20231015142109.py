from django.shortcuts import render,redirect
from .models import Histoire
from django.contrib import messages

def index(request):
    #histoire= Histoire.objects.all().count()
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
        a=Histoire(nom_region=nom_region,nom_departement=nom_departement,
                 sous_prefecture=sous_prefecture,nom_village=nom_village,
                   nom_declarant=nom_declarant,prenon_declarant=prenon_declarant
                   ,qualite_declarant=qualite_declarant,date_naissance_declarant=date_naissance_declarant,
                   lieu_naissance_declarant=lieu_naissance_declarant,
                   lieu_residence_declarant=lieu_residence_declarant)
        a.save()
        messages.success(request, 'Book was uploaded successfully')
        return redirect('index')
    else:
        messages.error(request, 'Book was not uploaded successfully')
        return render(request, 'forms/forms.html')

def  formulairetranscription(request):
    return render(request,'forms/transcription/transcription.html')

