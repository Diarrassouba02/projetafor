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


@login_required(login_url='connection')
def index(request):
    histoire= Histoire.objects.all()
    lien_persone=Histoire.objects.filter(accord_passe='Non').count()
    lien_persone_non=floatformat(lien_persone*100/len(histoire), 2)
    act=Histoire.objects.filter(acte_creation='non').count()
    actp=floatformat(act*100/len(histoire), 2)
    nrg= len(Histoire.objects.values('nom_region').distinct())
    ndp= len(Histoire.objects.values('nom_departement').distinct())
    nsp= len(Histoire.objects.values('sous_prefecture').distinct())
    #mode accè_terre
    mode_acces = Histoire.objects.values('mode_accès_terre').annotate(
        nb=Count('mode_accès_terre', distinct=True)).order_by('-nb')[:5]

    labels3 = [item['mode_accès_terre'] for item in mode_acces]
    data3 = [item['nb'] for item in mode_acces]

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
    labels = [entry['region'] for entry in data]
    nbdepartements = [entry['nbdepartements'] for entry in data]
    nbsous_prefectures = [entry['nbsousprefectures'] for entry in data]
    nbvillages=[entry['nbvillages'] for entry in data]
    context={"labels":labels,'region': region_name,
    "histoire":histoire,'nbdepartements': nbdepartements,
    'nbsous_prefectures': nbsous_prefectures,
    'nbvillages': nbvillages,'ndp':ndp,'nsp':nsp,'nrg':nrg,
    'labels1': labels1, 'data1': data1,'labels2': labels2, 'data2': data2,
    'labels3': labels3, 'data3': data3,'actp':actp,'lien_persone_non':lien_persone_non}
    #contex={}
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


#Genération du rapport pdf

def rapport_pdf(request, pk):
    histoire=Histoire.objects.get(id=pk)
    histoire.succeseur_nom_prenon_date=ast.literal_eval(histoire.succeseur_nom_prenon_date)
    histoire.nomlignage=ast.literal_eval(histoire.nomlignage)
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
    c.rect(1*cm, 1*cm,540, 28*cm)
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
    paragraphe.wrapOn(c, 530,40)
    paragraphe.drawOn(c, 1.2 * cm, 2.5*cm)

    c.setFillColor(colors.green)
    c.rect(1 * cm, 14*cm, 540, 0.80*cm, fill=True)
    c.setFillColorRGB(1, 1, 1)  # Blanc en RGB
    c.rect(1.1 * cm, 14 * cm, 80, 18, fill=True)
    c.setFillColor(colors.black)
    c.drawString(4.5*cm,14.5*cm,"Qui a fondé le village? Quelle état son activité principale? où à t'il été inhumé?")
    c.drawString(1.2*cm,14.5*cm,"Question N°2")
    paragraphe1= Paragraph(text_lines8, style)
    paragraphe1.wrapOn(c, 530,40)
    paragraphe1.drawOn(c, 1.2 * cm, 15*cm)
    c.drawString(1*cm,840,"EODTV 2")
    c.drawString(19*cm,840,"page2")
    c.showPage()

    #troisième page
    c.setStrokeColor(colors.green)
    c.rect(1*cm, 1*cm,540, 28*cm)
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
    paragraphe2.wrapOn(c, 530,40)
    paragraphe2.drawOn(c, 1.2 * cm, 3.5*cm)

    c.setFillColor(colors.green)
    c.rect(1 * cm, 14*cm, 540, 0.80*cm, fill=True)
    c.setFillColorRGB(1, 1, 1)  # Blanc en RGB
    c.rect(1.1 * cm, 14 * cm, 80, 18, fill=True)
    c.setFillColor(colors.black)
    c.drawString(4.5*cm,14.5*cm,"A quelle époque l'installation s'est faite ici?")
    c.drawString(1.2*cm,14.5*cm,"Question N°4")
    paragraphe1= Paragraph(text_lines10, style)
    paragraphe1.wrapOn(c, 530,40)
    paragraphe1.drawOn(c, 1.2 * cm, 15.5*cm)
    c.drawString(1*cm,840,"EODTV 2")
    c.drawString(19*cm,840,"page3")
    c.showPage()

    #quatrième page
    c.setStrokeColor(colors.green)
    c.rect(1*cm, 1*cm,540, 28*cm)
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
    paragraphe1.wrapOn(c, 530,40)
    paragraphe1.drawOn(c, 1.2 * cm, 18*cm)
    c.drawString(1*cm,840,"EODTV 2")
    c.drawString(19*cm,840,"page4")
    c.showPage()
    #cinquième page
    c.setStrokeColor(colors.green)
    c.rect(1*cm, 1*cm,540, 28*cm)
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
    paragraphe2.wrapOn(c, 530,40)
    paragraphe2.drawOn(c, 1.2 * cm, 3.5*cm)
    c.setFillColor(colors.green)
    c.rect(1 * cm, 16*cm, 540, 1.2*cm, fill=True)
    c.setFillColorRGB(1, 1, 1)  # Blanc en RGB
    c.rect(1.1 * cm, 16 * cm, 80, 18, fill=True)
    c.setFillColor(colors.black)
    c.drawString(4.5*cm,16.5*cm,"Combien de lignages se réclament d'un ancêtre commun?")
    c.drawString(4.5*cm,17*cm,"Quel est l'ordre d'arrivé de ces lignages?")
    c.drawString(1.2*cm,16.5*cm,"Question N°8")
    paragraphe1= Paragraph(text_lines12, style)
    paragraphe1.wrapOn(c, 530,40)
    paragraphe1.drawOn(c, 1.2 * cm, 18*cm)
    c.drawString(1*cm,840,"EODTV 2")
    c.drawString(19*cm,840,"page5")



    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='proces_verbale.pdf')


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
        lien_persone_non=floatformat(lien_persone*100/len(histoire), 2)
        act=histoires_region.filter(acte_creation='non').count()
        actp=floatformat(act*100/len(histoire), 2)
    else:
        return render(request, 'visualisation.html')
    context={'labels':labels,'nbsp':nbsp,'nbv':nbv,'data1':data1,
    'labels2':labels2,'data2':data2,'data3':data3,'labels3':labels3,
    'lien_persone_non':lien_persone_non,'labels4':labels4,
    'data4':data4,'actp':actp,'nom_regions_select': nom_regions_select}
    return render(request, 'visualisation.html',context)