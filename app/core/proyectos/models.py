from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField

from userdata.models import DatosUser

# Create your models here.
class TipoDocu(models.Model):
    NombTiDoc = models.CharField(max_length=45, verbose_name="Nombre Tipo Documento")
    
    class Meta:
        verbose_name = "Tipos de Documento"
        verbose_name_plural = "Tipos de Documento"
        
    def __str__(self):
        return self.NombTiDoc
        
class CategProye(models.Model):
    lenguaje = models.CharField(max_length=45, verbose_name="Lenguaje")
    motorDB = models.CharField(max_length=155, verbose_name="Motor de Base de Datos")
    arquitectura = models.CharField(max_length=255, verbose_name="Arquitectura")
    
    class Meta:
        verbose_name="Categoria del Proyecto"
        verbose_name_plural = "Información Especifica del Proyecto"
        
    def __str__(self):
        return self.lenguaje
    
class Proyectos(models.Model):
    idCategProye = models.ForeignKey(CategProye, on_delete = models.CASCADE, verbose_name="Identificador de Categoria")
    nombProy = models.CharField(max_length=255, verbose_name="Nombre del Proyecto")
    descProy = models.TextField(max_length=255, verbose_name="Descripción del Proyecto")
    imgProy = models.ImageField(default='proyecto.png', upload_to= None, verbose_name="Foto del Proyecto")
    fechaIni = models.DateField(null = True, verbose_name="Iniciado el")
    fechaFin = models.DateField(null = True, verbose_name="Finalizado el")
    urlRepo = models.CharField(max_length=255, verbose_name="Dirección Repositorio")
    estaProy = models.CharField(max_length=45, verbose_name="Estado del Proyecto")
    
    class Meta:
        verbose_name = "Descripción Proyectos"
        verbose_name_plural = "Descripción Proyectos"
        
    def __str__(self):
        return self.nombProy    
    
class Documentos(models.Model):
    idTipoDocu = models.ForeignKey(TipoDocu, on_delete = models.CASCADE, verbose_name="Identificador de Tipo Documento")
    idUsuarios = models.ForeignKey(DatosUser, on_delete = models.CASCADE, verbose_name="Identificador de Usuario")
    idProyectos = models.ForeignKey(Proyectos, on_delete = models.CASCADE, verbose_name="Identificador de Proyectos")
    nombDocu = models.CharField(max_length=155, null = False, verbose_name="Nombre del Documento")
    pathDocu = models.FileField(upload_to= None, verbose_name="Documento")
    
    class Meta:
        verbose_name = "Documentos"
        verbose_name_plural = "Documentos"
        
    def __str__(self):
        return self.nombDocu



        