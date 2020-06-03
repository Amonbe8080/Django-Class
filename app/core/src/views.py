from django.views.generic.base import TemplateView
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

class HomePageView(TemplateView):

    template_name = "index.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'titulo':'Digital Market', 
                                                    'frase':'Tu mejor opción',
                                                    'descripcion':'Digital market es un plataforma de ventas para un supermercado acogiendo un diseño acogedor y fácil de usar para el usuario, la plataforma contará con diversas opciones tanto para el usuario y administrador.',
                                                    
                                                    'tituloPrincipal':'¿Por qué nosotros?', 
                                                    
                                                    'titulo1': 'Producto personalizado según tu mercado',
                                                    'desc1': 'Los colores y categorías serán completamente personalizados, estará adecuado  según el color seleccionado o podrás escoger entre las categorias y los iconos que tendrá tu sitio web.', 
                                                    
                                                    'titulo2': 'Fa  cilidad de manejo',
                                                    'desc2': 'Se mostraran los pedidos más recientes y podrás cambiar el estado de cada uno de ellos con un solo botón.', 
                                                    
                                                    'titulo3': 'Asistencia personal y remota',
                                                    'desc3': 'Nuestro equipo de ayuda está dispuesto 24/7 a resolver tus problemas o inquietudes sobre el manejo de nuestra plataforma.', 
                                                    
                                                    'titulo4': 'Implementación personal',
                                                    'desc4': 'Nuestros asesores estarán allí explicándote como funciona el aplicativo y como hacer una correcta implementación de este mismo.', 
                                                    
                                                    'titulo5': 'Adaptable a móviles',
                                                    'desc5': 'Tu sitio web será visualizado de manera correcta desde computadores de mesa, Tablet o dispositivos móviles.',
                                                    
                                                    'titulo6': 'Soporte de la web',
                                                    'desc6': 'Tu sitio web podrá soportar más de 50+ usuarios al mismo tiempo realizando una interacción constante con la página.'})
    
class NosotrosPageView(TemplateView):
    
    template_name = "nosotros.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'titulo1': '¿Quienes Somos?',
                                                    
                                                    'direccion': 'Complejo Norte, Medellín, Antioquia, Carrera 68 #104, CO',
                                                    'celular': '+54 314 541 58 78',
                                                    'correo': 'helpdesk@digitalmarket.com',
                                                    
                                                    'miembro1': 'Sebastian Alvarez Perez', 
                                                    'perfil1': 'Desarrollador Backend',
                                                    'correo1': 'alvarezperezsebastian2014@gmail.com',
                                                    
                                                    'miembro2': 'Tomas Diaz Vasquez', 
                                                    'perfil2': 'Desarrollador Frontend',
                                                    'correo2': 'samot0051@gmail.com',
                                                    
                                                    'miembro3': 'Kevin Alexander Suaza Gomez', 
                                                    'perfil3': 'Desarrollador Backend',
                                                    'correo3': 'kealsugo@gmail.com'})

# Vista basada en funcion
def contacto(request):
    formContact = ContactForm()
    
    #Validar que el formulario tenga una peticion post
    if request.method == "POST":
        # Rellenamos la plantilla del formulario
        formContact = ContactForm(data=request.POST)
        if formContact.is_valid():
            tipomsj = request.POST.get('tipomsj','')
            usuario = request.POST.get('usuario','')
            correo = request.POST.get('correo','')
            mensaje = request.POST.get('mensaje','')
            
            # Crear objeto con las variables del formulario
            email = EmailMessage(
                "Digital Market: Tienes un mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(usuario, correo, mensaje),
                "no-contestar@inbox.mailtrap.io",
                ["alvarezperezsebastian2014@gmail.com"],
                reply_to=[correo]
            )
            
            # Enviar correo
            try:
                email.send()
                return redirect(reverse('contacto')+"?ok")
            except:
                # Error al enviar correo
                return redirect(reverse('contacto')+"?fail")
            
            
            
    
    return render(request, 'contacto.html', {'formulario':formContact})

