from django.shortcuts import render
from .models import DatosUser

# Create your views here.
from django.views.generic.list import ListView

class DatosUserListView(ListView):
    model = DatosUser
    template_name = "nosotros.html"
    def get_context_data(self, **kwargs):
        context = super(DatosUserListView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is just some data'
        return context
    
