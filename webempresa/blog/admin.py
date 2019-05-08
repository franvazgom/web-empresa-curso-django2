from django.contrib import admin
from .models import Category, Post
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    #https://docs.djangoproject.com/en/2.0/ref/contrib/admin/#modeladmin-options 

    list_display = ('title', 'author', 'published', 'post_categories')
    ordering = ('author', 'published')
    #Para un solo elemento: ordering = ('author', )
    #search_fields = ('title','content') #Busca en las columnas de titulo y contenido
    search_fields = ('title','content', 'author__username', 'categories__name') #EN el author busca el campo "usrename"
    date_hierarchy = 'published'
    list_filter = ('author__username','categories__name')

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by('name')])

    post_categories.short_description = "Categorías"
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)