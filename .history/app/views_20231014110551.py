from django.shortcuts import render,redirect
from .models import Histoire
from django.contrib import messages

def index(request):
    #histoire= Histoire.objects.all().count()
    return render(request, 'index.html')


# Forms
def formulairemanuscrit(request):
    if request.method=='POST':
        nom_region=request.POST['region']
        nom_departement=request.POST['departement']
        sous_prefecture=request.POST['sous_prefecture']
        nom_village=request.POST['nom_village']
        a=Histoire(nom_region=nom_region,nom_departement=nom_departement,sous_prefecture=sous_prefecture,nom_village=nom_village)
        print(a.tojson)
        messages.success(request, 'Book was uploaded successfully')
        return redirect('index')
    else:
        messages.error(request, 'Book was not uploaded successfully')
        return render(request, 'forms/forms.html')



