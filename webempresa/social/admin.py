from django.contrib import admin
from .models import Link 
# Register your models here.

class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    #Para extender la funcionalidad en tiempo de ejecución
    #Para poder persoalizar los privilegios en ADMIN
    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Personal").exists():
            #return ('created', 'updated', 'key', 'name')
            return ('key', 'name')
        else:
            return ('created', 'updated')
        
admin.site.register(Link, LinkAdmin)