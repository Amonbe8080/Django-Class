from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from .genero import Generos

# Create your models here.
class Roles(models.Model):
    RoleName = models.CharField(max_length=50, verbose_name="Nombre de Perfil")
    
    class Meta: 
        verbose_name = "Perfiles de Usuario"
        verbose_name_plural = "Perfiles"
    
    def __str__(self):
        return self.RoleName
    
class DatosUser(models.Model):
    userDNI = models.CharField(max_length=20, verbose_name="Identificación")
    nombUser = models.CharField(max_length=20, null = True, verbose_name="Nombres")
    apelUser = models.CharField(max_length=20, null = True, verbose_name="Apellidos")
    profeUser = models.CharField(max_length=100, null = True, verbose_name="Profesión")
    fotoUser = models.ImageField(default='user.png', upload_to= "img/perfiles", verbose_name="Foto de perfil")
    teleUser = models.CharField(max_length=20, verbose_name="Número de Teléfono")
    geneUser = models.CharField(max_length=20, choices= Generos, default = "Otro", verbose_name="Género")
    
    adddata = models.DateTimeField(auto_now_add = True, null = True, verbose_name="Creado el")
    modifiat = models.DateTimeField(auto_now = True, null = True, verbose_name="Modificado el")
    
    class Meta: 
        verbose_name = "Datos del Usuario"
        verbose_name_plural = "Informacíon"

    # Definimos la funcion 
    def __str__(self):
        return self.nombUser+" "+self.apelUser

class HabilUser(models.Model):
    NombHabi=models.CharField(max_length=100, verbose_name="Nombre de la Competencia")
    DescHabi= models.TextField(verbose_name="Descripción de la Competencia")
    
    class Meta: 
        verbose_name = "Habilidades del Usuario"
        verbose_name_plural = "Competencias"
     
    # definimos la funcion 
    def __str__(self):
        return self.NombHabi
    
class DetaRoles(models.Model):
    idRole = models.ForeignKey(Roles, on_delete = models.CASCADE, verbose_name="Identificador de Rol")
    idUser = models.ForeignKey(DatosUser, on_delete = models.CASCADE, verbose_name="Identificación de Usuario")
    addUser = models.DateTimeField(auto_now_add = True, auto_now = False)
    udtuser = models.DateTimeField(auto_now = True, null = True)
    estaRol = models.CharField(max_length=10)
    
    class Meta: 
        verbose_name = "Roles de Usuario"
        verbose_name_plural = "Roles"
    
    def __str__(self):
        return self.idUser
    
class Rates(models.Model):
    idHabil = models.ForeignKey(HabilUser, on_delete = models.CASCADE, verbose_name="Identificador de Habilidad")
    idUser = models.ForeignKey(DatosUser, on_delete = models.CASCADE, verbose_name="Identificador de Usuario")
    prcHabil = models.DecimalField(max_digits=2, decimal_places = 1, verbose_name="Porcentaje de Habilidad")
    udtHabil = models.DateTimeField(auto_now = True, null = True)
    
    class Meta: 
        verbose_name = "Nivel de Habilidad"
        verbose_name_plural = "Niveles de Usuario"

     # definimos la funcion 
    def __str__(self):
        return self.idUser
 