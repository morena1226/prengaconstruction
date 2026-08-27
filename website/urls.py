from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sherbimet/', views.content_page, {'page': 'services'}, name='services'),
    path('projektet/', views.content_page, {'page': 'projects'}, name='projects'),
    path('rreth-nesh/', views.content_page, {'page': 'about'}, name='about'),
    path('kontakt/', views.content_page, {'page': 'contact'}, name='contact'),
    path('projekti/<int:pk>/', views.project_detail, name='project_detail'),
]
