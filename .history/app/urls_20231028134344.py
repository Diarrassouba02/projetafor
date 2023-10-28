from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('formulairemanuscrit/',views.formulairemanuscrit,name='formulairemanuscrit'),
    path('formulairetranscription/',views.formulairetranscription,name='formulairetranscription'),

    ]


