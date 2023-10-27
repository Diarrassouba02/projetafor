from django.shortcuts import render
#from .models import Histoire

def index(request):
    #histoire= Histoire.objects.all().count()
    return render(request, 'index.html')


# Forms
def formulairemanuscrit(request):
    return render(request, 'forms/forms.html')


