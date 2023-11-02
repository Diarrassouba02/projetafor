from django.urls import path

from . import views

urlpatterns = [

    path("", views.connection, name="connection"),
    path("index", views.index, name="index"),
    path('connection',views.formulairemanuscrit,name='connection'),
    path("datah", views.datatables, name="datah"),
    path('logout', views.logout_view, name='logout'),


    ]


