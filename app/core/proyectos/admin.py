from django.contrib import admin
from .models import TipoDocu, CategProye, Proyectos, Documentos

# Register your models here.
class TipoDocuModel(admin.ModelAdmin):
    list_display = ["NombTiDoc"]
    
    class Meta: 
        model = TipoDocu
        
admin.site.register(TipoDocu)

class CategProyeModel(admin.ModelAdmin):
    list_display = ["lenguaje"]
    
    class Meta: 
        model = CategProye
        
admin.site.register(CategProye)

class ProyectosModel(admin.ModelAdmin):
    list_display = ["nombProy"]
    
    class Meta: 
        model = Proyectos
        
admin.site.register(Proyectos)

class DocumentosModel(admin.ModelAdmin):
    list_display = ["nombDocu"]
    
    class Meta: 
        model = Documentos
        
admin.site.register(Documentos)