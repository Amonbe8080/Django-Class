from django.contrib import admin
from .models import Roles, DetaRoles, HabilUser, Rates, DatosUser

# Register your models here.

class RoleModel(admin.ModelAdmin):
    list_display = ["RoleName"]
    list_display_links = ["RoleName"]
    list_filter = ["RoleName"]
    
    class Meta: 
        model = Roles
        
admin.site.register(Roles)

class DatosUserModel(admin.ModelAdmin):
    list_display = ["nombUser"]
    
    class Meta: 
        model = DatosUser
        
admin.site.register(DatosUser)

class DetaRolesModel(admin.ModelAdmin):
    list_display = ["idRole"]
    
    class Meta: 
        model = DetaRoles

admin.site.register(DetaRoles)

class HabiUserModel(admin.ModelAdmin):
    list_display = ["NombHabi"]
    
    class Meta: 
        model = HabilUser
        
admin.site.register(HabilUser)

class RatesModel(admin.ModelAdmin):
    list_display = ["idUser"]
    
    class Meta: 
        model = Rates
        
admin.site.register(Rates)
