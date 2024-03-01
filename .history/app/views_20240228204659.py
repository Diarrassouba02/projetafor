from django.shortcuts import render,redirect,get_object_or_404
from django.templatetags.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.auth.decorators import login_required
from .models import Histoire
from django.contrib import messages,auth
from django.contrib.auth import authenticate,logout
import ast,io
from django.http import FileResponse
import reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from PIL import Image
from reportlab.lib import colors
from django.db.models import Count
from django.template.defaultfilters import floatformat
from reportlab.platypus import SimpleDocTemplate, Preformatted
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph
from datetime import datetime
import json

@login_required(login_url='connection')
def index(request):
    histoire= Histoire.objects.all()
    text1 = "Village de Abo Kouadio Village de agro Kouadiokro Montagne Mère des Barala Inconnu Colatier Oeil pour oeil dent pour dent Village islamique Village de Vacaba Le nom Aka-Djémélékro provient proviens du nom son de fondateur du nom de Gnandji Aka qui a pour surnom Djouemelé c'est à dire le plus gros silure. Consideré comme un homme fort c'est pourquoi le village porte le nom Aka-Djémélékro Nom du Fondateur Nom Mère du Fondateur Mise en Garde Village de Séko Village de Zoumassa Villade d'Akaffou Femme Rive de la Bagoué Opposant des mauvais esprits Inconnu Le village D'Aka Kouamé Le village de Alliali Village de Angan Koffi Assankro vient du nom de son fondateur Kouadio Koua. C'est pour cela que l'on disait à l'époque Kouadio koua Assankro devenu plus tard Assankro Konan Yaa Nom-Village Village de Bendé-Tanou Village de Kouamé-Konan Génie bienfaiteur Village de Yao-Loukou Solidarité-Union Village de Ouffoué Village de Ouffouet Village de Kouassi Kongo Village de N'Da-N'Guessan Hospitalité Village de Agro Kouadio Mariage en Famille Marche Forêt des Panthères Arbre à Palabre Village de Kouakou Adi Village de Nin Soleil Qui Brille Rivière Komoro Lieu De Mon Choix Village De Bliglala Sortons De La Brousse Argile Rouge Voir Se Reposer Ici Village De N'Gbankoun Parc e Boeuf Village De Kouassi Village de Tiassé Forcer Village De Tioumou Près De La Mosquée Village De Brouillard Village de L'arbre Taba Village De Djémé Nom Père Fondateur Bli Rivière Sia Village De Boyao Milieu D'une Rivière Nom Fondateur Nom Fondateur Forêt D'Or Quand Arriverai-Je Réseaux Village De Kokoti Kouamé Village De Ahoua Sous Les Cocotiers Reine A Eu Des Problèmes Nom du Fondateur Feuille de Melon Gande Forêt Bangolo signifie terre de prospérité et Kahen signifie rendre son cadre de vie sain et nettoyer ses alentours Pied de la montagne Gan Chez Dani Emplacement De La Corde Kpeuh Au Milieu Des Arbres Gbon Village vaste et épais Bouobly signifie village fondé par Bouo Village Situé Sur La Montagne Guian Le nom du village signifie :village situé entre quatre villages et 4 buts Tribus Nom Du Fondateur Village situé en bas d'une montagne appeler Zetro Le nom du village est Diéou. Diéou vient du mot Dilérou qui signifie un lieu rencontrer par hasard un site intéressant à retrouver brusquement qui a servi à l'installation du village c'est la transcription de l'administration qui est Diéou Changement De Lieux Village De Dankouan Essuyer Les Larmes Bon Village Désert Chez Gbanto Village De Touo Village situé au pied du Mont Glan Terre de Paix Indépendance Village De Biégbaha Proximité Du Bois zdzdz Séparer L'un De L' Autre Termitière Rouge En Worodougou En Bas D'une Montagne au nom de Douan Fleuve Le Village Porte Le Nom Du Fondateur Qui S'Appelait Mangangnan En Bas DE l'Arbre Gba Village Du Marabout Termitière Village De Ban Fiman La Montagne Ou Habitaient Les Goris Sous La Forêt Village De Gueutagbeu Va T'Asseoir Chez Sivi Village De Ouattara Sous Le Fromager Bois Petite Eau Claire, Limpide Dieu Est Grand Le Village Des Dioula Village De Paix Débordement De L'eau De Son Nid Nouveau Village Nom Du Fondateur Kpan-Fleungbeu Chez Les Chefs Village De Gopou Commerçants Village De Djiguiba Village De Dangba Inconnu Union Du Village Village De Touo L' Endroit Où Il Fait Chaud Site De Rassemblement Chez Gba Bossieu Sous L' Arbre Respect De La Parole Donnée Sanctionner Le Redoutable Homme Se Frotter Au Centre Arbre Village De Guerriers La Guerre Est Finie Village De Blah Village De Bienfaisance Village De La Jeune Propriétaire De L'eau Pimenté Village De Koi Village Entre Les Rivières Village De Bassa Village De Bako Village De Gboto Village De Tra Village De Lê"

    #text1="""Village de Abo Kouadio Village de agro Kouadiokro Montagne Mère des Barala Inconnu Colatier Oeil
    #kolo kolo kolo"""
    #text1 = ' '.join(his.signification for his in histoire)
    #print(text1)
    #on compte les objet ou accord_passe=Non.
    lien_persone=Histoire.objects.filter(accord_passe='Non').count()
    lien_persone_non=floatformat(lien_persone*100/len(histoire), 2)
    #idem
    act=Histoire.objects.filter(acte_creation='non').count()
    actp=floatformat(act*100/len(histoire), 2)
    #idem
    chef_terre=Histoire.objects.filter(chef_terre='oui').count()
    chefoui=floatformat(chef_terre*100/len(histoire), 2)
    #idem
    lien=Histoire.objects.filter(lien='').count()
    liennul=floatformat(lien*100/len(histoire), 2)

    # on compte le nombre de region depertement et sous_préfecture
    nrg= len(Histoire.objects.values('nom_region').distinct())
    ndp= len(Histoire.objects.values('nom_departement').distinct())
    nsp= len(Histoire.objects.values('sous_prefecture').distinct())
    #on retient que la varianbe mode acces on compte le nombre de modalité.
    mode_acces = Histoire.objects.values('mode_accès_terre').annotate(
        nb=Count('mode_accès_terre', distinct=True)).order_by('-nb')[:5]


    quad=Histoire.objects.values('qualite_declarant').annotate(
        nb=Count('qualite_declarant', distinct=True)).order_by('-nb')[:10]
    dataquad=[item['nb'] for item in quad]
    labelsquad=[item['qualite_declarant'] for item in quad]

    epoqued= Histoire.objects.values('epoque_installation').annotate(
        nb=Count('epoque_installation', distinct=True)).order_by('-nb')[:5]
    labelsepoque = [item['epoque_installation'] for item in epoqued]
    dataepoque = [item['nb'] for item in epoqued]

    activite_fon= Histoire.objects.values('activite_fondateur').annotate(
        nb=Count('activite_fondateur', distinct=True)).order_by('-nb')[:5]


    dateoff= Histoire.objects.values('dateoff').annotate(
        nb=Count('dateoff', distinct=True)).order_by('-nb')[:5]
    dataoff=[item['nb'] for item in dateoff]
    labelsoff=[item['dateoff'] for item in dateoff]

    autoriteoff= Histoire.objects.values('autoriteoff').annotate(
        nb=Count('autoriteoff', distinct=True)).order_by('-nb')[:5]
    labelsauoff = [item['autoriteoff'] for item in autoriteoff]
    dataauoff = [item['nb'] for item in autoriteoff]

    labels3 = [item['mode_accès_terre'] for item in mode_acces]
    data3 = [item['nb'] for item in mode_acces]

    labelsactfon = [item['activite_fondateur'] for item in activite_fon]
    dataactfon = [item['nb'] for item in activite_fon]

    #diagramme mise_a_la_disposition_terre
    mise_a_disp = Histoire.objects.values('mode_mise_a_diposition').annotate(
        nb=Count('mode_mise_a_diposition', distinct=True)).order_by('-nb')[:5]
    labels2 = [item['mode_mise_a_diposition'] for item in  mise_a_disp]
    data2 = [item['nb'] for item in  mise_a_disp]

    #diagramme personne_trouvée
    pertrouve_data = Histoire.objects.values('personne_trouve').annotate(
        nbpertrouve=Count('personne_trouve', distinct=True))
    labels1 = [item['personne_trouve'] for item in pertrouve_data]
    data1 = [item['nbpertrouve'] for item in pertrouve_data]

    #Obtenez les données agrégées à partir du modèle Histoire
    nomregions = Histoire.objects.values('nom_region').distinct()

    data = []
    for nomregion in nomregions:
        region_name = nomregion['nom_region']
        nbdepartements =len(set(Histoire.objects.filter(nom_region=region_name).values_list('nom_departement', flat=True)))
        nbsous_prefectures = len(set(Histoire.objects.filter(nom_region=region_name).values_list('sous_prefecture', flat=True)))
        nbvillages = len(set(Histoire.objects.filter(nom_region=region_name).values_list('nom_village', flat=True)))
        nbqualitedeclreg=len(set(Histoire.objects.filter(nom_region=region_name).values_list('qualite_declarant', flat=True)))
        data.append({
            'region': region_name,
            'nbdepartements': nbdepartements,
            'nbsousprefectures': nbsous_prefectures,
            'nbvillages': nbvillages,

        })
#   Etude anciens sites région
    regan=Histoire.objects.values('nom_region','ancien_site')
    count_by_region = {}
    for element in regan:
        element['ancien_site'] = ast.literal_eval(element['ancien_site'])
        count_by_region[element['nom_region']] = count_by_region.get(element['nom_region'], 0) + len(element['ancien_site'])
    # Etude site d'adoration de la région
    regsite=Histoire.objects.values('nom_region','site_adoration')
    dicregsite = {}
    for element in regsite:
        element['site_adoration'] = ast.literal_eval(element['site_adoration'])
        dicregsite[element['nom_region']] = dicregsite.get(element['nom_region'], 0) + len(element['site_adoration'])
    # Etude Nombre de successeur regions
    regsuc=Histoire.objects.values('nom_region','succeseur_nom_prenon_date')
    dicregsuc = {}
    for element in regsuc:
        element['succeseur_nom_prenon_date'] = ast.literal_eval(element['succeseur_nom_prenon_date'])
        dicregsuc[element['nom_region']] = dicregsuc.get(element['nom_region'], 0) + len(element['succeseur_nom_prenon_date'])
    print(dicregsuc)
    # Etude nombre de lignage par regions
    regli=Histoire.objects.values('nom_region','nomlignage')
    dicregli = {}
    for element in regli:
        element['nomlignage'] = ast.literal_eval(element['nomlignage'])
        dicregli[element['nom_region']] = dicregli.get(element['nom_region'], 0) + len(element['nomlignage'])

    # Etude zone litigés
    reglitige=Histoire.objects.values('nom_region','limite_litige_village')
    for item in reglitige:
        item['limite_litige_village'] = ast.literal_eval(item['limite_litige_village'])
    nb_zones_litigieuses_non_vides_par_region = {}
    for item in reglitige:
        nom_region = item['nom_region']
        if nom_region not in nb_zones_litigieuses_non_vides_par_region:
             nb_zones_litigieuses_non_vides_par_region[nom_region] = 0
        for zone in item['limite_litige_village']:
           if zone['zone_litigee']=='oui' or zone['zone_litigee']=='Oui':
              nb_zones_litigieuses_non_vides_par_region[nom_region] += 1
    resultat_final = dict(nb_zones_litigieuses_non_vides_par_region)
    # les labels
    labels = [entry['region'] for entry in data]
    nbdepartements = [entry['nbdepartements'] for entry in data]
    nbsous_prefectures = [entry['nbsousprefectures'] for entry in data]
    nbvillages=[entry['nbvillages'] for entry in data]
    context={"labels":labels,'region': region_name,
    "histoire":histoire,'nbdepartements': nbdepartements,
    'nbsous_prefectures': nbsous_prefectures,
    'nbvillages': nbvillages,'ndp':ndp,'nsp':nsp,'nrg':nrg,
    'labels1': labels1, 'data1': data1,'labels2': labels2, 'data2': data2,
    'labels3': labels3, 'data3': data3,'actp':actp,'lien_persone_non':lien_persone_non,
    'labelsquad':labelsquad,'dataquad':dataquad,'labelsepoque':labelsepoque,'dataepoque':
    dataepoque,'labelsoff':labelsoff,'dataoff': dataoff,'dataactfon':dataactfon,'labelsactfon':labelsactfon,
    'dataauoff':dataauoff,'labelsauoff':labelsauoff,'chefoui':chefoui,'chef_terre':chef_terre,
    'lien':lien,'liennul':liennul,'count_by_region':count_by_region,'text1':text1,'dicregsite':dicregsite}
    return render(request, 'index.html',context)




@login_required
def formulairemanuscrit(request):
    histoires= Histoire.objects.all()
    contexte={"histoires":histoires}
    if  request.method == 'POST':
        successor_count = int(request.POST.get('successor_count', 0))
        villagetrouve_count= int(request.POST.get('villagetrouve_count', 0))
        line_count = int(request.POST.get('line_count', 0))
        campement_count = int(request.POST.get('campement_count', 0))
        site_count = int(request.POST.get('site_count', 0))
        ancient_site_count = int(request.POST.get('ancient_site_count', 0))
        village_count = int(request.POST.get('village_count', 0))
        limite_village_litige_count = int(request.POST.get('limite_village_litige_count', 0))
        successors_data = []  # Créez une liste
        lines_data = []
        campements_data = []
        sites_data = []
        ancient_sites_data = []
        village_data = []
        limite_village_litige_data = []
        village_trouve_data=[]

        for i in range( successor_count):
            name = request.POST.get(f'name_{i}')
            first_name = request.POST.get(f'first_name_{i}')
            accession_date = request.POST.get(f'accessiondate_{i}')

            # Ajoutez les données de chaque successeur à la liste
            successor_data = {
                'nom': name,
                'prénom': first_name,
                'accession_date': accession_date
            }
            successors_data.append(successor_data)

        for i in range(line_count):
            name = request.POST.get(f'lineName_{i}')
            order = request.POST.get(f'lineOrder_{i}')
            line_data = {
                'nom_lignage': name,
                "ordre": order,
            }
            lines_data.append(line_data)

        for i in range(campement_count):
            name = request.POST.get(f'campementName_{i}')
            peuple = request.POST.get(f'campementPeuple_{i}')
            origine = request.POST.get(f'campementOrigine_{i}')

            campement_data = {
                'nom': name,
                'peuple': peuple,
                'origine': origine,
            }
            campements_data.append(campement_data)


        for i in range(site_count):
            name = request.POST.get(f'siteName_{i}')
            localisation = request.POST.get(f'localisation_{i}')
            site_data = {
                'name': name,
                'localisation': localisation,
            }
            sites_data.append(site_data)

        for i in range(ancient_site_count):
            name = request.POST.get(f'ancientSiteName_{i}')
            motif = request.POST.get(f'ancientSiteMotif_{i}')
            ancient_site_data = {
                'name': name,
                'motif': motif,
            }
            ancient_sites_data.append(ancient_site_data)


        for i in range(village_count):
            village_name = request.POST.get(f'villageName_{i}')
            village_data.append(village_name)

        for i in range(limite_village_litige_count):
            village = request.POST.get(f'village_{i}')
            limite = request.POST.get(f'limite_{i}')
            zone_litigee = request.POST.get(f'zoneLitigee_{i}')
            limite_village_litige_data.append({
                'village': village,
                'limite': limite,
                'zone_litigee': zone_litigee,
            })

        for i in range(villagetrouve_count):
            groupement_trouve=request.POST.get(f'villagetrouveName_{i}')
            village_trouve_data.append({'groupement':groupement_trouve})

        nom_region = request.POST.get('region')
        nom_departement = request.POST.get('department')
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
        dateoff=request.POST.get('dateoff')
        autoriteoff=request.POST.get('nomaut')
        acte_creation=request.POST.get('act')
        mode_accès_terre=request.POST.getlist('mode')
        chef_terre=request.POST.get('chef')
        mode_mise_a_diposition=request.POST.getlist('disposition')
        complement=request.POST.get ('complement')
        for histoire in histoires:
            if sous_prefecture==histoire.sous_prefecture and nom_village==histoire.nom_village:
                messages.error(request, 'village déja enregistré')
                return render(request, 'forms/forms.html')
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
                     accord_passe=accord_passe,epoque_installation=epoque_installation,
                     nomlignage=lines_data,dateoff=dateoff, autoriteoff= autoriteoff,
                     acte_creation=acte_creation,campement_nom_origine=campements_data,
                     site_adoration=sites_data,ancien_site=ancient_sites_data,
                     mode_accès_terre=mode_accès_terre,chef_terre=chef_terre,
                     mode_mise_a_diposition=mode_mise_a_diposition,groupement_liste=village_data,
                     limite_litige_village=limite_village_litige_data,complement=complement,
                     groupement_trouve=village_trouve_data)



        a.save()
        messages.success(request, "village enregistré avec succès")
        return redirect('formulairemanuscrit')
    else:
        return render(request, 'forms/forms.html')




def logout_view(request):
    logout(request)
    return redirect('connection')

def connection(request):
    user = request.user
    context = {'user': user}
    if request.method == 'POST':
        username=request.POST.get('username')
        last_name = request.POST.get('nom')
        first_name = request.POST.get('prenom')
        email=request.POST.get('email')
        password = request.POST.get('password')
        user =authenticate(request, password=password,username=username)
        if user is not None and user.is_active:
            auth.login(request, user)
            if  user.is_superuser and user.is_staff:
                return redirect('index')
            else:
                return redirect('index')
        else:
            error_message = "Nom d'utilisateur ou/et mot de passe incorrect."
            return render(request,'forms/transcription/transcription.html',{'message':error_message})
    else:
        return render(request,'forms/transcription/transcription.html',context)

# Tables


@login_required
def datatables(request):
    histoires= Histoire.objects.all()
    for histoire in histoires:
        histoire.mode_accès_terre=ast.literal_eval(histoire.mode_accès_terre)
        histoire.mode_mise_a_diposition=ast.literal_eval(histoire.mode_mise_a_diposition)
        histoire.limite_litige_village
        contexte={"histoires":histoires}
    return render(request, 'tables/datatables.html',contexte)

def detaille(request,pk):
    histoire=Histoire.objects.get(id=pk)
    histoire.campement_nom_origine=ast.literal_eval(histoire.campement_nom_origine)
    histoire.mode_mise_a_diposition=ast.literal_eval(histoire.mode_mise_a_diposition)
    histoire.mode_accès_terre=ast.literal_eval(histoire.mode_accès_terre)
    histoire.succeseur_nom_prenon_date=ast.literal_eval(histoire.succeseur_nom_prenon_date)
    histoire.limite_litige_village=ast.literal_eval(histoire.limite_litige_village)
    histoire.groupement_trouve=ast.literal_eval(histoire.groupement_trouve)
    histoire.nomlignage=ast.literal_eval(histoire.nomlignage)
    histoire.site_adoration=ast.literal_eval(histoire.site_adoration)
    histoire.ancien_site=ast.literal_eval(histoire.ancien_site)
    histoire.groupement_liste=ast.literal_eval(histoire.groupement_liste)
    contexte={"histoire":histoire}

    return render(request, 'detaille.html',contexte)



def modifier(request,pk):
    histoire = get_object_or_404(Histoire, pk=pk)
    date_naissance_declarant = histoire.date_naissance_declarant.strftime('%Y-%m-%d')
    histoires = Histoire.objects.filter(nom_region=histoire.nom_region)
    histoire1 = Histoire.objects.filter(nom_departement=histoire.nom_departement)
    histoire2 = Histoire.objects.filter(sous_prefecture=histoire.sous_prefecture)
    noms_departements = {histoire.nom_departement for histoire in histoires}
    noms_sp = {histoire.sous_prefecture for histoire in histoire1}
    noms_v = {histoire.nom_village for histoire in histoire2}
    context={'histoire':histoire,'noms_departements':noms_departements,'noms_sp':noms_sp,'noms_v':noms_v,'date_naissance_declarant':date_naissance_declarant}
    return render(request,'forms/modifier.html',context)


#Genération du rapport pdf

def rapport_pdf(request, pk):
    histoire=Histoire.objects.get(id=pk)
    histoire.succeseur_nom_prenon_date=ast.literal_eval(histoire.succeseur_nom_prenon_date)
    histoire.nomlignage=ast.literal_eval(histoire.nomlignage)
    histoire.campement_nom_origine=ast.literal_eval(histoire.campement_nom_origine)
    histoire.site_adoration=ast.literal_eval(histoire.site_adoration)
    histoire.ancien_site=ast.literal_eval(histoire.ancien_site)
    histoire.mode_mise_a_diposition=ast.literal_eval(histoire.mode_mise_a_diposition)
    histoire.mode_accès_terre=ast.literal_eval(histoire.mode_accès_terre)
    histoire.groupement_liste=ast.literal_eval(histoire.groupement_liste)
    histoire.limite_litige_village=ast.literal_eval(histoire.limite_litige_village)
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=A4, bottomup=0)
    image_path = "static/images/repuplique.jpg"
    image = Image.open(image_path)
    image = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    image_buf = io.BytesIO()
    image.save(image_buf, format='JPEG')

    text_lines = [
        "MINISTERE DE L'AGRICULTURE",
        "ET DU DEVELOPPEMENT RURAL"
    ]

    text_lines1=[
    f"1. Direction Régionale:  {histoire.nom_region}",
    f"2. Direction Départementale:  {histoire.nom_departement}",
    f"3. CGFR de la Sous-Préfecture:  {histoire.sous_prefecture}",
    f"4. CVGFR du village:  {histoire.nom_village}"]


    text_lines2 = ["PROCES-VERBAL"]
    text_lines3=["DE RECUEIL DE L'HISTORIQUE DE LA CONSTITUTION DU TERRITOIRE DU VILLAGE"]
    text_lines4=[f"DE: {histoire.nom_village}"]


    text_lines5=[f"Je soussigné {histoire.nomenq } {histoire.prenomenq}",
                 "Commissaire-enquêteur désigné, pour recueillir l'historique de la constitution du territoire du village",
                f"de {histoire.nom_village}",
   "me suis rendu au village ci-dessus mentionné et ai recueilli en présence des personnes dont la liste",
   "est en annexe les déclarations ci-après:"]

    text_lines6=[f"Nom et prénoms du déclarant: {histoire.nom_declarant } {histoire.prenon_declarant}",
                f"Date et lieu de naissance: {histoire.date_naissance_declarant } à {histoire.lieu_naissance_declarant}",
                f"Qualité: {histoire.qualite_declarant }",
                f"Lieu de résidence: {histoire.lieu_residence_declarant }"]



    text_lines7=f"Le nom du village est {histoire.nom_village}, qui signifie {histoire.signification}."
    text_lines8=f"Le village à été fondé par {histoire.nom_fondateur} {histoire.prenom_fondateur}, sont activitée principale: {histoire.activite_fondateur}, lieu d'inhumation: {histoire.lieu_inhimationf}."
    if histoire.origine_fondateur:
       text_lines9=""
       if histoire.personne_trouve=="Aucune":
          text_lines9=f"L'origine du fondateur est:{histoire.origine_fondateur} il n'a trouvé personnes sur les lieux."
       else:
            if histoire.lien:
                text_lines9=f"L'origine du fondateur est:{histoire.origine_fondateur}, il à trouvé un {histoire.personne_trouve}.A t'il passé des accords? {histoire.accord_passe},lien avec les personnes trouvées:{histoire.lien}."
            else:
                text_lines9=f"L'origine du fondateur est:{histoire.origine_fondateur}, il à trouvé un {histoire.personne_trouve}.A t'il passé des accords? {histoire.accord_passe}.Pas de lien avec les personnes trouvées."
    else:
        text_lines9=""
        if histoire.personne_trouve=="Aucune":
           text_lines9=f"L'origine du fondateur est inconnue il n'a trouvé personnes sur les lieux."
        else:
            if histoire.lien:
                text_lines9=f"L'origine du fondateur est inconnue, il à trouvé un {histoire.personne_trouve}.A t'il passé des accords? {histoire.accord_passe},lien avec les personnes trouvées:{histoire.lien}."
            else:
                text_lines9=f"L'origine du fondateur est inconnue, il à trouvé un {histoire.personne_trouve}.A t'il passé des accords? {histoire.accord_passe}.Pas de lien avec les personnes trouvées."

    text_lines10=f"Epoque d'installation: {histoire.epoque_installation}."
    text_lines11=""
    for i in histoire.succeseur_nom_prenon_date:
        if i["nom"]:
           if i["prénom"]:
              if i["accession_date"]:
                 text_lines11=f'({i["nom"]} {i["prénom"]}, {i["accession_date"]}).'+text_lines11
                 #suc.append({'nom': i["nom"],'prénom':i["prénom"],'accession_date':i["accession_date"],})
              else:
                  text_lines11=f'({i["nom"]} {i["prénom"]}, Inconnue).'+text_lines11
           else:
                if i["accession_date"]:
                 text_lines11=f'({i["nom"]}, Inconnu, {i["accession_date"]}).'+text_lines11

                else:
                    text_lines11=f'({i["nom"]} ,Inconnu, Inconnue).'+text_lines11

        else:
            if i["prénom"]:
              if i["accession_date"]:
                 text_lines11=f'(Inconnu ,{i["prénom"]}, {i["accession_date"]}).'+text_lines11
              else:
                  text_lines11=f'(Inconnu, {i["prénom"]}, Inconnue).'+text_lines11
            else:
                if i["accession_date"]:
                   text_lines11=f'(Inconnu ,Inconnu, {i["accession_date"]}).'+text_lines11
                else:
                    text_lines11=f'(Inconnu; Inconnu, Inconnue).'+text_lines11

    text_lines12=""
    for i in histoire.nomlignage:
        if i['nom_lignage']:
            if i['ordre']:
               text_lines12=f"{i['nom_lignage']},N°{i['ordre']};"+' '+text_lines12
            else:
                text_lines12=f"{i['nom_lignage']},Ordre Inconnu;"+' '+text_lines12
        else:
            if i['ordre']:
               text_lines12=f"Lignage inconnu, N°{i['ordre']};"+' '+text_lines12
            else:
                text_lines12=f"Lignage inconnu,Ordre Inconnu;"+' '+text_lines12

    text_lines13=""
    if histoire.dateoff:
       if histoire.autoriteoff:
          text_lines13=f"La localité est érigée en village officiellement en: {histoire.dateoff}. Par {histoire.autoriteoff}. Pouvez-vous produire l'acte de création? la reponse est: {histoire.acte_creation}"+text_lines13
       else:
            text_lines13=f"La localité est érigée en village officiellement en: {histoire.dateoff}. Par inconnu. Pouvez-vous produire l'acte de création? la reponse est: {histoire.acte_creation}"+text_lines13
    else:
        if histoire.autoriteoff:
          text_lines13=f"La localité est érigée en village officiellement en:inconnu. Par {histoire.autoriteoff}. Pouvez-vous produire l'acte de création? la reponse est: {histoire.acte_creation}"+text_lines13
        else:
            text_lines13=f"La localité est érigée en village officiellement en: inconnu. Par inconnu. Pouvez-vous produire l'acte de création? la reponse est: {histoire.acte_creation}"+text_lines13

    text_lines14=""
    for i in histoire.campement_nom_origine:
        if i['peuple']:
           if i['nom']:
               if i['origine']:
                   text_lines14=f"Le nombre de campement est:{len(histoire.campement_nom_origine)}.(Nom du campement: {i['nom']} Peuple: {i['peuple']}, origine de ce peuple: { i['origine']}). "+text_lines14
               else:
                   text_lines14=f"Le nombre de campement est:{len(histoire.campement_nom_origine)}.(Nom du campement: {i['nom']}, Peuple: {i['peuple']},  origine de ce peuple: Origine Inconnu.) "+text_lines14
           else:
                if i['origine']:
                   text_lines14=f"Le nombre de campement est:{len(histoire.campement_nom_origine)}.(Nom du campement: inconnu, Peuple: {i['peuple']},origine de ce peuple: { i['origine']}). "+text_lines14
                else:
                   text_lines14=f"Le nombre de campement est:{len(histoire.campement_nom_origine)}.(Nom du campement: inconnu, Peuple: {i['peuple']},  origine de ce peuple: Origine Inconnu.)"+text_lines14
        else:
            if i['nom']:
               if i['origine']:
                   text_lines14=f"Le nombre de campement est:{len(histoire.campement_nom_origine)}.(Nom du campement: {i['nom']},Peuple: Inconnu,  origine de ce peuple: { i['origine']}.) "+text_lines14
               else:
                   text_lines14=f"Le nombre de campement est:{len(histoire.campement_nom_origine)}.(Nom du campement: {i['nom']},Peuple: Inconnu, origine de ce peuple: Origine Inconnu)."+text_lines14
            else:
                if i['origine']:
                   text_lines14=f"Le nombre de campement est:{len(histoire.campement_nom_origine)}.(Nom du campement: inconnu, Peuple: Inconnu,origine de ce peuple: { i['origine']}). "+text_lines14
                else:
                   text_lines14="Le village n'a aucun campement"

    text_lines15=""
    if histoire.site_adoration:
       for i in histoire.site_adoration:
           text_lines15=f"site: {i['name']},localisation:{i['localisation']}."+'  '+' '+text_lines15

    else:
        text_lines15="Pas de site d'adoration."

    text_lines16=""
    if histoire.ancien_site:
       for i in histoire.ancien_site:
           text_lines16=f"site: {i['name']},Motif:{i['motif']}."+'  '+' '+text_lines16

    else:
        text_lines16="Pas d'anciens sites."

    text_lines17=""
    if histoire.mode_accès_terre:
       for i in histoire.mode_accès_terre:
           text_lines17=f"{i} "+ ' '+text_lines17
    else:
        text_lines17="Inconnu"

    text_lines18=""
    if histoire.mode_mise_a_diposition:
       for i in histoire.mode_mise_a_diposition:
           text_lines18=f"{i} "+ ' '+text_lines18
    else:
        text_lines18="Inconnu"


    text_lines19=""
    if histoire.groupement_liste[0]:
       for i in histoire.groupement_liste:
           text_lines19=f" {i} "+ ' '+text_lines19
    else:
        text_lines19="Le village ne provient pas du groupement de plusieurs villages"

    text_lines20=""
    for i in histoire.limite_litige_village:
        text_lines20=f"({i['village']})"+'  '+text_lines20

    text_lines21=""
    for i in histoire.limite_litige_village:
        text_lines21=f"(village voisin:{i['village']}-limite:{i['limite']})"+text_lines21

    text_lines22=""
    a=0
    for i in histoire.limite_litige_village:
        if i['zone_litigee']:
           a=1
           text_lines22=f" (Village:{i['village']}-limite {i['limite']}-litige {i['zone_litigee']})"+text_lines22
        if a==0:
           text_lines22="Nous n'avons aucun litige avec les villages voisins."
    if histoire.complement:
       text_lines23=f"{histoire.complement}"
    else:
        text_lines23='RAS'
    text=c.beginText()
    text.setTextOrigin(1*cm,250)
    for line in text_lines:
        text.textLine(line)
    c.drawText(text)
    c.setStrokeColor(colors.green)
    c.setFillColor(colors.green)
    c.line(1 * cm, 528, 20.04 * cm, 528)
    c.rect(1 * cm, 12.3 * cm, 540, 2 * cm, fill=True)

    text2 = c.beginText()
    text2.setFillColorRGB(0.1,0.1,0.1)
    text2.setTextOrigin(17.2*cm/2 ,365)
    for line in text_lines2:
        text2.textLine(line)
    c.drawText(text2)


    text3 = c.beginText()
    text3.setFillColorRGB(0.1,0.1,0.1)
    text3.setTextOrigin(4.3*cm/2 ,380)
    for line in text_lines3:
        text3.textLine(line)
    c.drawText(text3)





    text4 = c.beginText()
    text4.setFillColorRGB(0.1,0.1,0.1)
    text4.setTextOrigin(4.3*cm/2 ,395)
    for line in text_lines4:
        text4.textLine(line)
    c.drawText(text4)

    text5 = c.beginText()
    text5.setTextOrigin(1.2*cm ,450)
    for line in text_lines5:
        text5.textLine(line)
    c.setStrokeColor(colors.green)
    c.rect(1*cm, 14.3*cm,540, 14*cm)
    c.drawText(text5)


    text6 = c.beginText()
    l=550
    lt=545
    for line in text_lines6:
        text6.setTextOrigin(1.2*cm ,lt)
        c.setFont("Helvetica-Bold", 12)
        text6.textLine(line)
        c.line(1 * cm, l, 20.04 * cm, l)
        l=l+20
        lt=lt+20

    c.drawText(text6)
    c.setStrokeColor(colors.black)
    c.line(1.5 * cm, 740, 6*cm, 740)
    c.setFont("Helvetica", 12)
    c.drawString(1.5*cm,750,"Nota Bene: indiquer après la déclaration en manuscrit la mention suivante:")
    c.drawString(1.5*cm,765,"«lecture faite à M....................................... qui persisre et signe le...................à ............................».")
    c.drawString(1*cm,820,"EODTV 2")
    c.drawString(19*cm,820,"page1")


    text1=c.beginText()
    text1.setTextOrigin(1.2*cm,290)
    for line in text_lines1:
        text1.textLine(line)
    c.setStrokeColor(colors.green)
    c.rect(1*cm, 9.7*cm,540, 2.3*cm)
    c.drawText(text1)


    c.drawImage(ImageReader(image_buf),(A4[0] - 250) / 2,2*cm,width=250, height=150)
    c.showPage()
    #deuxieme page
    c.setStrokeColor(colors.green)
    c.rect(1*cm, 1*cm,540, 27.5*cm)
    c.setFillColor(colors.green)
    c.rect(1 * cm, 1 * cm, 540, 0.80*cm, fill=True)
    c.setFillColorRGB(1, 1, 1)  # Blanc en RGB
    c.rect(1.1 * cm, 1.1 * cm, 80, 18, fill=True)
    c.setFillColor(colors.black)
    c.drawString(4.5*cm,1.5*cm,"Quel est le nom du village ? Quelle est sa signification?")
    c.drawString(1.2*cm,1.5*cm,"Question N°1")
    style = getSampleStyleSheet()['Normal']
    style.fontName = 'Helvetica'
    style.fontSize = 12
    c.setFont("Helvetica", 12)
    paragraphe = Paragraph(text_lines7, style)
    paragraphe.wrapOn(c, 530,400)
    paragraphe.drawOn(c, 1.2 * cm, 2.5*cm)

    c.setFillColor(colors.green)
    c.rect(1 * cm, 14*cm, 540, 0.80*cm, fill=True)
    c.setFillColorRGB(1, 1, 1)  # Blanc en RGB
    c.rect(1.1 * cm, 14 * cm, 80, 18, fill=True)
    c.setFillColor(colors.black)
    c.drawString(4.5*cm,14.5*cm,"Qui a fondé le village? Quelle état son activité principale? où à t'il été inhumé?")
    c.drawString(1.2*cm,14.5*cm,"Question N°2")
    paragraphe1= Paragraph(text_lines8, style)
    paragraphe1.wrapOn(c, 530,400)
    paragraphe1.drawOn(c, 1.2 * cm, 15*cm)
    c.drawString(1*cm,830,"EODTV 2")
    c.drawString(19*cm,830,"page2")
    c.showPage()

    #troisième page
    c.setStrokeColor(colors.green)
    c.rect(1*cm, 1*cm,540, 27.5*cm)
    c.setFillColor(colors.green)
    c.rect(1 * cm, 1 * cm, 540, 1.7*cm, fill=True)
    c.setFillColorRGB(1, 1, 1)  # Blanc en RGB
    c.rect(1.1 * cm, 1.1 * cm, 80, 18, fill=True)
    c.setFillColor(colors.black)
    c.drawString(4.3*cm,1.5*cm,"D'où venait-il ? A-t-il trouvé des personnes sur les lieux ? Si oui,lesquelles (villages,")
    c.drawString(4.3*cm,2*cm,"groupement de personnes)? A-t-il passé des accords avec ces derniers? ")
    c.drawString(4.3*cm,2.5*cm,"Qu'est ce qui les liait au fondateur?")
    c.drawString(1.2*cm,1.5*cm,"Question N°3")
    paragraphe2=Paragraph(text_lines9, style)
    paragraphe2.wrapOn(c, 530,400)
    paragraphe2.drawOn(c, 1.2 * cm, 3.5*cm)

    c.setFillColor(colors.green)
    c.rect(1 * cm, 14*cm, 540, 0.80*cm, fill=True)
    c.setFillColorRGB(1, 1, 1)  # Blanc en RGB
    c.rect(1.1 * cm, 14 * cm, 80, 18, fill=True)
    c.setFillColor(colors.black)
    c.drawString(4.5*cm,14.5*cm,"A quelle époque l'installation s'est faite ici?")
    c.drawString(1.2*cm,14.5*cm,"Question N°4")
    paragraphe1= Paragraph(text_lines10, style)
    paragraphe1.wrapOn(c, 530,400)
    paragraphe1.drawOn(c, 1.2 * cm, 15.5*cm)
    c.drawString(1*cm,830,"EODTV 2")
    c.drawString(19*cm,830,"page3")
    c.showPage()

    #quatrième page
    c.setStrokeColor(colors.green)
    c.rect(1*cm, 1*cm,540, 27.5*cm)
    c.setFillColor(colors.green)
    c.rect(1 * cm, 1 * cm, 540, 1.2*cm, fill=True)
    c.setFillColorRGB(1, 1, 1)  # Blanc en RGB
    c.rect(1.1 * cm, 1.1 * cm, 80, 18, fill=True)
    c.setFillColor(colors.black)
    c.drawString(4.3*cm,1.5*cm,"Quels sont les noms des chefs qui se sont succédés à la tête du village?")
    c.drawString(4.3*cm,2*cm," pouvez-vous nous donner les dates d'accession au pouvoir de ces chefs?")
    c.drawString(1.2*cm,1.5*cm,"Question N°5")
    c.drawString(1.2*cm,2.7*cm,"La liste des successeurs dans l'ordre nom, prénom, date accession:")
    paragraphe1= Paragraph(text_lines11, style)
    paragraphe1.wrapOn(c, 530,400)
    paragraphe1.drawOn(c, 1.2 * cm, 2.8*cm)

    c.setFillColor(colors.green)
    c.rect(1 * cm, 16*cm, 540, 1.2*cm, fill=True)
    c.setFillColorRGB(1, 1, 1)  # Blanc en RGB
    c.rect(1.1 * cm, 16 * cm, 80, 18, fill=True)
    c.setFillColor(colors.black)
    c.drawString(4.5*cm,16.5*cm,"Combien de lignages se réclament d'un ancêtre commun?")
    c.drawString(4.5*cm,17*cm,"Quel est l'ordre d'arrivé de ces lignages?")
    c.drawString(1.2*cm,16.5*cm,"Question N°6")
    paragraphe1= Paragraph(text_lines12, style)
    paragraphe1.wrapOn(c, 530,400)
    paragraphe1.drawOn(c, 1.2 * cm, 18*cm)
    c.drawString(1*cm,830,"EODTV 2")
    c.drawString(19*cm,830,"page4")
    c.showPage()
    #cinquième page
    c.setStrokeColor(colors.green)
    c.rect(1*cm, 1*cm,540, 27.5*cm)
    c.setFillColor(colors.green)
    c.rect(1 * cm, 1 * cm, 540, 1.7*cm, fill=True)
    c.setFillColorRGB(1, 1, 1)  # Blanc en RGB
    c.rect(1.1 * cm, 1.1 * cm, 80, 18, fill=True)
    c.setFillColor(colors.black)
    c.drawString(4.3*cm,1.5*cm,"Depuis quand Ia localité est erigee en village officiellement? Par quelle autorité ")
    c.drawString(4.3*cm,2*cm,"a-t-elle été erigee (Administration du territoire, ARSO, AVB etc.) ")
    c.drawString(4.3*cm,2.5*cm,"Pouvez-vous produire l'acte de création?")
    c.drawString(1.2*cm,1.5*cm,"Question N°7")
    paragraphe2=Paragraph(text_lines13, style)
    paragraphe2.wrapOn(c, 530,400)
    paragraphe2.drawOn(c, 1.2 * cm, 3.5*cm)

    c.setFillColor(colors.green)
    c.rect(1 * cm, 14*cm, 540, 1.2*cm, fill=True)
    c.setFillColorRGB(1, 1, 1)  # Blanc en RGB
    c.rect(1.1 * cm, 14 * cm, 80, 18, fill=True)
    c.setFillColor(colors.black)
    c.drawString(4.5*cm,14.5*cm,"Ce village a-t-il des campements ? Si oui, Quel en est le nombre ? Voulez-vous")
    c.drawString(4.5*cm,15*cm," également nous indiquer les origines de ces populations?")
    c.drawString(1.2*cm,14.5*cm,"Question N°8")
    paragraphe1= Paragraph(text_lines14, style)
    paragraphe1.wrapOn(c, 530,400)
    paragraphe1.drawOn(c, 1.2 * cm, 16*cm)
    c.drawString(1*cm,830,"EODTV 2")
    c.drawString(19*cm,830,"page5")
    c.showPage()
    #sixième page
    c.setStrokeColor(colors.green)
    c.rect(1*cm, 1*cm,540, 27.5*cm)
    c.setFillColor(colors.green)
    c.rect(1 * cm, 1 * cm, 540, 1.2*cm, fill=True)
    c.setFillColorRGB(1, 1, 1)  # Blanc en RGB
    c.rect(1.1 * cm, 1.1 * cm, 80, 18, fill=True)
    c.setFillColor(colors.black)
    c.drawString(4.3*cm,1.5*cm,"Le village possède t'il des sites d'oration ? (fore collines, savane, cours d'eau).?")
    c.drawString(4.3*cm,2*cm,"Les citer et indiquer leur localisation?")
    c.drawString(1.2*cm,1.5*cm,"Question N°9")
    paragraphe1= Paragraph(text_lines15, style)
    paragraphe1.wrapOn(c, 530,400)
    paragraphe1.drawOn(c, 1.2 * cm, 3*cm)

    c.setFillColor(colors.green)
    c.rect(1 * cm, 14*cm, 540, 1.2*cm, fill=True)
    c.setFillColorRGB(1, 1, 1)  # Blanc en RGB
    c.rect(1.1 * cm, 14 * cm, 82, 18, fill=True)
    c.setFillColor(colors.black)
    c.drawString(4.5*cm,14.5*cm,"Y a-t-il un ou plusieurs ancien(s) site(s) du villages ?si oui, Quels sont les motifs")
    c.drawString(4.5*cm,15*cm,"du (des) transfert(s)")
    c.drawString(1.2*cm,14.5*cm,"Question N°10")
    paragraphe1= Paragraph(text_lines16, style)
    paragraphe1.wrapOn(c, 530,400)
    paragraphe1.drawOn(c, 1.2 * cm, 16*cm)
    c.drawString(1*cm,830,"EODTV 2")
    c.drawString(19*cm,830,"page6")
    c.showPage()
    #septieme page
    c.setStrokeColor(colors.green)
    c.rect(1*cm, 1*cm,540, 27.5*cm)
    c.setFillColor(colors.green)
    c.rect(1 * cm, 1 * cm, 540, 1.2*cm, fill=True)
    c.setFillColorRGB(1, 1, 1)  # Blanc en RGB
    c.rect(1.1 * cm, 1.1 * cm, 82, 18, fill=True)
    c.setFillColor(colors.black)
    c.drawString(4.3*cm,1.5*cm,"Quels sont les modes d'accès à Ia terre ? Y a-t-il un chef de terre ? Comment se")
    c.drawString(4.3*cm,2*cm,"fait la mise à la disposition des terres ' (heritage, don, prêt, achat, location)")
    c.drawString(1.2*cm,1.5*cm,"Question N°11")
    c.drawString(1.2*cm,3*cm,"Mode d'accès à la terre:")
    c.drawString(1.2*cm,4*cm,"Mise à la disposition de la terre:")
    paragraphe1= Paragraph(text_lines17, style)
    paragraphe2= Paragraph(text_lines18, style)
    paragraphe1.wrapOn(c, 530,400)
    paragraphe2.wrapOn(c, 530,400)
    paragraphe1.drawOn(c, 1.2 * cm, 3.5*cm)
    paragraphe2.drawOn(c, 1.2 * cm, 4.5*cm)

    c.setFillColor(colors.green)
    c.rect(1 * cm, 14*cm, 540, 0.80*cm, fill=True)
    c.setFillColorRGB(1, 1, 1)  # Blanc en RGB
    c.rect(1.1 * cm, 14 * cm, 82, 18, fill=True)
    c.setFillColor(colors.black)
    c.drawString(4.5*cm,14.5*cm,"Ce village-ci provient-il du regroupement de deux ou plusieurs villages? citez les")
    c.drawString(1.2*cm,14.5*cm,"Question N°12")
    paragraphe1= Paragraph(text_lines19, style)
    paragraphe1.wrapOn(c, 530,400)
    paragraphe1.drawOn(c, 1.2 * cm, 16*cm)
    c.drawString(1*cm,830,"EODTV 2")
    c.drawString(19*cm,830,"page7")
    c.showPage()
    #huitieme page
    c.setStrokeColor(colors.green)
    c.rect(1*cm, 1*cm,540, 27.5*cm)
    c.setFillColor(colors.green)
    c.rect(1 * cm, 1 * cm, 540, 0.80*cm, fill=True)
    c.setFillColorRGB(1, 1, 1)  # Blanc en RGB
    c.rect(1.1 * cm, 1.1 * cm, 82, 18, fill=True)
    c.setFillColor(colors.black)
    c.drawString(4.5*cm,1.5*cm,"Citez les villages qui sont vos voisins?")
    c.drawString(1.2*cm,1.5*cm,"Question N°13")
    paragraphe1= Paragraph(text_lines20, style)
    paragraphe1.wrapOn(c, 530,400)
    paragraphe1.drawOn(c, 1.2 * cm, 3*cm)

    c.setFillColor(colors.green)
    c.rect(1 * cm, 14*cm, 540, 1.2*cm, fill=True)
    c.setFillColorRGB(1, 1, 1)  # Blanc en RGB
    c.rect(1.1 * cm, 14 * cm, 82, 18, fill=True)
    c.setFillColor(colors.black)
    c.drawString(4.5*cm,14.5*cm,"Pouvez-vous nous indiquer les limites des terres de votre village? (rivière, limite de")
    c.drawString(4.5*cm,15*cm,"nettoyage de Ia piste, un gros arbre, une colline, un bas fonds)?")
    c.drawString(1.2*cm,14.5*cm,"Question N°14")
    paragraphe1= Paragraph(text_lines21, style)
    paragraphe1.wrapOn(c, 530,40)
    paragraphe1.drawOn(c, 1.2 * cm, 15*cm)
    c.drawString(1*cm,830,"EODTV 2")
    c.drawString(19*cm,830,"page8")
    c.showPage()
    #neuvième page
    c.setStrokeColor(colors.green)
    c.rect(1*cm, 1*cm,540, 27*cm)
    c.setFillColor(colors.green)
    c.rect(1 * cm, 1 * cm, 540, 0.80*cm, fill=True)
    c.setFillColorRGB(1, 1, 1)  # Blanc en RGB
    c.rect(1.1 * cm, 1.1 * cm, 82, 18, fill=True)
    c.setFillColor(colors.black)
    c.drawString(4.5*cm,1.5*cm,"Existe-t-il des zones litigleuses sur les limites avec les villages voisins?")
    c.drawString(1.2*cm,1.5*cm,"Question N°15")
    paragraphe1= Paragraph(text_lines22, style)
    paragraphe1.wrapOn(c, 530,400)
    paragraphe1.drawOn(c, 1.2 * cm, 2.5*cm)

    c.setFillColor(colors.green)
    c.rect(1 * cm, 14*cm, 540, 0.80*cm, fill=True)
    c.setFillColorRGB(1, 1, 1)  # Blanc en RGB
    c.rect(1.1 * cm, 14 * cm, 82, 18, fill=True)
    c.setFillColor(colors.black)
    c.drawString(4.5*cm,14.5*cm,"Avez-vous des informations complémentaires a donner ?.")
    c.drawString(1.2*cm,14.5*cm,"Question N°16")
    paragraphe1= Paragraph(text_lines23, style)
    paragraphe1.wrapOn(c, 530,400)
    paragraphe1.drawOn(c, 1.2 * cm, 16*cm)
    c.line(1 * cm, 680, 20.04 * cm, 680)
    c.drawString(1.5*cm,700,"Enquete close le...........................................................")
    c.drawString(1.5*cm,750,"Signature du déclarant")
    c.drawString(12.5*cm,750,"Signature du Commissaire-Enqueteur")
    c.drawString(1*cm,810,"Comité Villageois de Gestion Foncière Rurale de...........................................................")
    c.drawString(1*cm,830,"EODTV 2")
    c.drawString(19*cm,830,"page9")

    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='procès-verbal.pdf')


def visualisationt(request):
    data=[]
    data1=[]
    if  request.method == 'POST':
        nom_regions_select = request.POST.get('region')
        data=[]
        histoires_region= Histoire.objects.filter(nom_region=nom_regions_select)
        for depatement in histoires_region.values('nom_departement').distinct():
            depatement_name =depatement['nom_departement']
            departement_data = {
                'nom_region': nom_regions_select,
                'nom_departement':depatement_name,
                'nbsp': len(set(histoires_region.filter(nom_departement= depatement_name).values_list('sous_prefecture', flat=True))),
                'nbv': len(set(histoires_region.filter(nom_departement= depatement_name).values_list('nom_village', flat=True)))
            }
            data.append(departement_data)
        labels = [item['nom_departement'] for item in data]
        nbsp = [item['nbsp'] for item in data]
        nbv=[item['nbv'] for item in data]
        #personnes trouvées
        pertrouve_data = histoires_region.values('personne_trouve').annotate(
                nbpertrouve=Count('personne_trouve', distinct=True))
        labels2 = [item['personne_trouve'] for item in pertrouve_data]
        data2 = [item['nbpertrouve'] for item in pertrouve_data]

        mode_acces = histoires_region.values('mode_accès_terre').annotate(
        nb=Count('mode_accès_terre', distinct=True)).order_by('-nb')[:5]
        labels3 = [item['mode_accès_terre'] for item in mode_acces]
        data3 = [item['nb'] for item in mode_acces]

        epoqued= histoires_region.values('epoque_installation').annotate(
        nb=Count('epoque_installation', distinct=True)).order_by('-nb')[:5]
        labelsepoque = [item['epoque_installation'] for item in epoqued]
        dataepoque = [item['nb'] for item in epoqued]

        quad=histoires_region.values('qualite_declarant').annotate(
        nb=Count('qualite_declarant', distinct=True)).order_by('-nb')[:5]
        dataquad=[item['nb'] for item in quad]
        labelsquad=[item['qualite_declarant'] for item in quad]

        dateoff= histoires_region.values('dateoff').annotate(
        nb=Count('dateoff', distinct=True)).order_by('-nb')[:5]
        dataoff=[item['nb'] for item in dateoff]
        labelsoff=[item['dateoff'] for item in dateoff]

        autoriteoff=  histoires_region.values('autoriteoff').annotate(
        nb=Count('autoriteoff', distinct=True)).order_by('-nb')[:5]
        labelsauoff = [item['autoriteoff'] for item in autoriteoff]
        dataauoff = [item['nb'] for item in autoriteoff]

        activite_fon= histoires_region.values('activite_fondateur').annotate(
        nb=Count('activite_fondateur', distinct=True)).order_by('-nb')[:5]
        labelsactfon = [item['activite_fondateur'] for item in activite_fon]
        dataactfon = [item['nb'] for item in activite_fon]

        lien=histoires_region.filter(lien='').count()
        liennul=floatformat(lien*100/len(histoires_region), 2)

        chef_terre=histoires_region.filter(chef_terre='oui').count()
        chefoui=floatformat(chef_terre*100/len(histoires_region), 2)


        #diagramme mise_a_la_disposition_terre
        mise_a_disp = histoires_region.values('mode_mise_a_diposition').annotate(
        nb=Count('mode_mise_a_diposition', distinct=True)).order_by('-nb')[:5]
        labels4 = [item['mode_mise_a_diposition'] for item in  mise_a_disp]
        data4 = [item['nb'] for item in  mise_a_disp]


        for sp in histoires_region.values('sous_prefecture','nom_departement').distinct():
            sous_prefecture_name =sp['sous_prefecture']
            departement= sp['nom_departement']
            departement_data = {
                'dep':departement,
                'nom_sp': sous_prefecture_name,
                'nbv1': len(set(histoires_region.filter(sous_prefecture= sous_prefecture_name).values_list('nom_village', flat=True)))
            }
            data1.append(departement_data)


        histoire= Histoire.objects.all()
        lien_persone=histoires_region.filter(accord_passe='Non').count()
        nbvilege=len(histoires_region)
        lien_persone_non=floatformat(lien_persone*100/len(histoires_region), 2)
        act=histoires_region.filter(acte_creation='non').count()
        actp=floatformat(act*100/len(histoires_region), 2)
    else:
        return render(request, 'visualisation.html')
    context={'labels':labels,'nbsp':nbsp,'nbv':nbv,'data1':data1,
    'labels2':labels2,'data2':data2,'data3':data3,'labels3':labels3,
    'lien_persone_non':lien_persone_non,'labels4':labels4,
    'data4':data4,'actp':actp,'nom_regions_select': nom_regions_select,
    'act':act,'lien_persone':lien_persone,'nbvilege':nbvilege,'labelsepoque':labelsepoque,
    'dataepoque':dataepoque,'dataquad':dataquad,'labelsquad':labelsquad,'dataoff':dataoff,
    'labelsoff':labelsoff,'labelsauoff':labelsauoff,'dataauoff':dataauoff,'labelsactfon':labelsactfon,
    'dataactfon':dataactfon,'lien':lien,'liennul':liennul,'chef_terre':chef_terre,'chefoui':chefoui}
    return render(request, 'visualisation.html',context)