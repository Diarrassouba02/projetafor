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



@login_required(login_url='connection')
def index(request):
    histoire= Histoire.objects.all().count()
    contex={"histoire":histoire}
    return render(request, 'index.html',contex)




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
            if  user.is_superuser and user.is_staff  :
                return redirect('index')
            else:
                return redirect('formulairemanuscrit')
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
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=A4, bottomup=0)
    image_path = "static/images/repuplique.jpg"
    image = Image.open(image_path)
    image = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    image_buf = io.BytesIO()
    image.save(image_buf, format='JPEG')
    c.setFont("Helvetica", 12)
    text_lines = [
        "MINISTERE DE L'AGRICULTURE",
        "ET DU DEVELOPPEMENT RURAL"
    ]

    text_lines1=[
    f"1. Direction Régionale:  {histoire.nom_region}",
    f"2. Direction Départementale:  {histoire.nom_departement}",
    f"3. CGFR de la Sous-Préfecture:  {histoire.sous_prefecture}",
    f"4. CVGFR du village:  {histoire.nom_village}"]



    titre1=["PROCES-VERBAL"]
    titre2=["DE RECUEIL DE L'HISTORIQUE DE LA CONSTITUTION DU TERRITOIRE DU VILLAGE"]
    titre3=["DE"]






    text1=c.beginText()
    text1.setTextOrigin(1*cm,250)
    for line in text_lines:
        text1.textLine(line)
    c.drawText(text1)
    text2=c.beginText()
    text2.setTextOrigin(1.2*cm,290)

    c.setStrokeColor(colors.green)
    c.setFillColor(colors.green)
    c.rect(1*cm, 9.7*cm,540, 2.3*cm,fillcolor=colors.aqua)


    for line in text_lines1:
        text2.textLine(line)



    c.drawText(text2)
    c.drawImage(ImageReader(image_buf),(A4[0] - 250) / 2,2*cm,width=250, height=150)
    c.drawString(200,200,"titre1")
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='proces_verbale.pdf')