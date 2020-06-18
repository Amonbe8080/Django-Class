from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('contacto/', views.contacto, name='contacto'),
]
