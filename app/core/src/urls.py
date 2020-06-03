from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('nosotros/', views.NosotrosPageView.as_view(), name='nosotros'),
    path('contacto/', views.contacto, name='contacto')
]
