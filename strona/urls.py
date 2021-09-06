from django.urls import path
from django.conf.urls import url
from . import views 

urlpatterns = [
    path('', views.glowna, name='glowna'),
    path('yerba_list', views.yerba_list, name='yerba_list'),
    path('yerba/<int:pk>/', views.yerba_detail, name='yerba_detail'),
    path('yerba/new', views.yerba_new, name='yerba_new'),
    path('yerba/<int:pk>/edit/', views.yerba_edit, name='yerba_edit'),
    path('yerba/<int:pk>/remove/', views.yerba_remove, name='yerba_remove'),
    path('yerba/<int:pk>/zatwierdzenie/', views.yerba_zatwierdzenie, name='yerba_zatwierdzenie'),
    path('piwo_list', views.piwo_list, name='piwo_list'),
    path('piwo/<int:pk>/', views.piwo_detail, name='piwo_detail'),
    path('piwo/new', views.piwo_new, name='piwo_new'),
    path('piwo/<int:pk>/edit/', views.piwo_edit, name='piwo_edit'),
    path('piwo/<int:pk>/remove/', views.piwo_remove, name='piwo_remove'),
    path('piwo/<int:pk>/zatwierdzenie/', views.piwo_zatwierdzenie, name='piwo_zatwierdzenie'),
    path('wino_list', views.wino_list, name='wino_list'),
    path('wino/<int:pk>/', views.wino_detail, name='wino_detail'),
    path('wino/new', views.wino_new, name='wino_new'),
    path('wino/<int:pk>/edit/', views.wino_edit, name='wino_edit'),
    path('wino/<int:pk>/remove/', views.wino_remove, name='wino_remove'),
    path('wino/<int:pk>/zatwierdzenie/', views.wino_zatwierdzenie, name='wino_zatwierdzenie'),
    path('kawa_list', views.kawa_list, name='kawa_list'),
    path('kawa/<int:pk>/', views.kawa_detail, name='kawa_detail'),
    path('kawa/new', views.kawa_new, name='kawa_new'),
    path('kawa/<int:pk>/edit/', views.kawa_edit, name='kawa_edit'),
    path('kawa/<int:pk>/remove/', views.kawa_remove, name='kawa_remove'),
    path('kawa/<int:pk>/zatwierdzenie/', views.kawa_zatwierdzenie, name='kawa_zatwierdzenie'),
    path('recenze_list', views.recenzje_list, name='recenzje_list'),
    url(r'^$', views.index, name='index'),
]