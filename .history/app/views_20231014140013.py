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
        #nom_village=request.POST.get('nom_village')
        print(nom_departement)
        print(sous_prefecture)
        a=Histoire(nom_region=nom_region,nom_departement=nom_departement,sous_prefecture=sous_prefecture)
        a.save()
        messages.success(request, 'Book was uploaded successfully')
        return redirect('index')
    else:
        messages.error(request, 'Book was not uploaded successfully')
        return render(request, 'forms/forms.html')



