from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto

admin.site.index_title = "Laboratorio"
admin.site.site_header = "Django administration"
admin.site.site_title = "Django site admin"

class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'laboratorio')

class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id','nombre',)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'laboratorio', 'get_f_fabricacion_year', 'p_costo', 'p_venta')
    list_filter = ('nombre', 'laboratorio')

    def get_f_fabricacion_year(self, obj):
        return obj.f_fabricacion.year if obj.f_fabricacion else None
    get_f_fabricacion_year.short_description = 'F Fabricación'

admin.site.register(DirectorGeneral,DirectorGeneralAdmin)
admin.site.register(Laboratorio,LaboratorioAdmin)
admin.site.register(Producto,ProductoAdmin)