from django.shortcuts import render,redirect
from .models import Histoire
from django.contrib import messages

def index(request):
    histoire= Histoire.objects.all().count()
    contex={"histoire":histoire}
    return render(request, 'index.html',contex)


# Forms
def formulairemanuscrit(request):
    if request.method == 'POST':
        successor_count = int(request.POST.get('successor_count', 0))
        successors_data = []  # Créez une liste

        for i in range(successor_count):
            name = request.POST.get(f'name_{i}')
            first_name = request.POST.get(f'first_name_{i}')
            accession_date = request.POST.get(f'accession_date_{i}')

            # Ajoutez les données de chaque successeur à la liste
            successor_data = {
                'name': name,
                'first_name': first_name,
                'accession_date': accession_date
            }
            successors_data.append(successor_data)

        nom_region = request.POST.get('region')
        nom_departement = request.POST.get('departement')
        sous_prefecture = request.POST.get('sous_prefecture')
        nomenq=request.POST.get('nomenq')
        prenomenq=request.POST.get('prenomenq')
        nom_village = request.POST.get('village')
        signification=request.POST.get('signification')
        nom_declarant = request.POST.get('nomdec')
        prenon_declarant = request.POST.get('prenomdec')
        qualite_declarant = request.POST.get('qualitedec')
        date_naissance_declarant = request.POST.get('datedec')
        lieu_naissance_declarant = request.POST.get('lieundec')
        lieu_residence_declarant = request.POST.get('lieudec')
        nom_fondateur = request.POST.get('nomf')
        prenom_fondateur = request.POST.get('prenomf')
        activite_fondateur = request.POST.get('activitef')
        origine_fondateur = request.POST.get('originef')
        lieu_inhimationf = request.POST.get('lieuinf')
        a = Histoire(nom_region=nom_region, nom_departement=nom_departement,
                     sous_prefecture=sous_prefecture, nom_village=nom_village,
                     nom_declarant=nom_declarant, prenon_declarant=prenon_declarant,
                     qualite_declarant=qualite_declarant, date_naissance_declarant=date_naissance_declarant,
                     lieu_naissance_declarant=lieu_naissance_declarant,
                     lieu_residence_declarant=lieu_residence_declarant,
                     nom_fondateur=nom_fondateur, prenom_fondateur=prenom_fondateur,
                     origine_fondateur=origine_fondateur, activite_fondateur=activite_fondateur,
                     lieu_inhimationf=lieu_inhimationf, succeseur_nom_prenon_date=successors_data)
        a.save()
        for data in successors_data:
            print(data)

        messages.success(request, 'Le formulaire a été soumis avec succès')
        return redirect('index')
    else:
        messages.error(request, 'Le formulaire n\'a pas été soumis avec succès')
        return render(request, 'forms/forms.html')
