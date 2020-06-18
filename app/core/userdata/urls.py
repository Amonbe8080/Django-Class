from django.urls import path
from .views import DatosUserListView

urlpatterns = [
    path('', DatosUserListView.as_view(), name='nosotros'),
]
