from django import forms
from .pqrsf import pqrsf

class ContactForm(forms.Form):
    # Atributos del formulario
    tipomsj= forms.ChoiceField(label="Tipo de petición", required=True, choices=pqrsf, widget=forms.Select(attrs={'class':'browser-default custom-select'}))
    usuario= forms.CharField(label="Nombre ", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'id':'contact-name'}))
    correo= forms.EmailField(label="Correo Electronico", required=True, widget=forms.EmailInput(attrs={'class':'form-control', 'id':'contact-email'}))
    mensaje= forms.CharField(label="Mensaje", required=True, widget=forms.Textarea(attrs={'class':'form-control md-textarea', 'id':'contact-message', 'rows':'3'}))
    