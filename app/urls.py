from django.urls import path

from . import views

urlpatterns = [

    path("", views.connection, name="connection"),
    path("index", views.index, name="index"),
    path('formulairemanuscrit/',views.formulairemanuscrit,name='formulairemanuscrit'),
    path("datah", views.datatables, name="datah"),
    path('logout', views.logout_view, name='logout'),
    path('detail<str:pk>', views.detaille, name='detail'),
    path('rapport<str:pk>', views.rapport_pdf, name='rapport'),
    path('visualisation', views.visualisationt, name='visualisation'),


    ]


