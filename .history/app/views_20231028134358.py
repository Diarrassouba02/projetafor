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
        successorCount = int(request.POST.get('successorCount', 0))
        successors_data = []  # Créez une liste

        for i in range(successorCount):
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
        lieu_inhimationf = request.POST.get('lieuinf')
        origine_fondateur = request.POST.get('originef')
        personne_trouve=request.POST.get('personne_trouve')
        accord_passe=request.POST.get('accord')
        lien=request.POST.get('lien')
        epoque_installation=request.POST.get('epoque')
        a = Histoire(nom_region=nom_region, nom_departement=nom_departement,
                     sous_prefecture=sous_prefecture, nom_village=nom_village,signification=signification,
                     nom_declarant=nom_declarant, prenon_declarant=prenon_declarant,
                     qualite_declarant=qualite_declarant, date_naissance_declarant=date_naissance_declarant,
                     lieu_naissance_declarant=lieu_naissance_declarant,
                     lieu_residence_declarant=lieu_residence_declarant,
                     nom_fondateur=nom_fondateur, prenom_fondateur=prenom_fondateur,
                     origine_fondateur=origine_fondateur, activite_fondateur=activite_fondateur,
                     lieu_inhimationf=lieu_inhimationf, succeseur_nom_prenon_date=successors_data,
                     nomenq=nomenq,prenomenq=prenomenq,personne_trouve=personne_trouve,lien=lien,
                     accord_passe=accord_passe,epoque_installation=epoque_installation)
        a.save()
        print(successorCount)

        messages.success(request, 'Le formulaire a été soumis avec succès')
        return redirect('index')
    else:
        messages.error(request, 'Le formulaire n\'a pas été soumis avec succès')
        return render(request, 'forms/forms.html')





def formulairetranscription(request):
    return redirect('index')