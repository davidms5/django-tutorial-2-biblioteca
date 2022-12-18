from django.contrib import admin

from .models import libro, Autor, genero, idiomas, libroInstance
# Register your models here.

#admin.site.register(libro)
class librosInstanceInline(admin.TabularInline):
    model = libroInstance
    extra = 0
    #esta clase hace que pueda incluir los datos del modelo libro instance en alguna otra clase de este archivo, como en libroAdmin. estaria encadenando modelos.
  #para mas info ver tabularInline en la documentacion de django
  
@admin.register(libro)
class libroAdmin(admin.ModelAdmin):
  
  
  list_display = ('titulo', 'autor', 'display_genero')
  inlines = [librosInstanceInline]
  
#admin.register.site(Autor, autorAdmin)  
#admin.site.register(Autor)

class librosPublicados(admin.TabularInline):
    model = libro
    extra = 1
    
  
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
  list_display = ('nombre', 'apellido', 'agno_nacimiento', 'fallecimiento')
  fields = ['apellido', 'nombre', ('agno_nacimiento', 'fallecimiento')]
  inlines = [librosPublicados]
  pass
  
admin.site.register(genero)

admin.site.register(idiomas)


#admin.site.register(libroInstance)
@admin.register(libroInstance)
class InstanceAdmin(admin.ModelAdmin):
  list_filter = ('status', 'devolucion')

  fieldsets = (
    ('datos del libro', {
      'fields':('libro', 'impreso', 'id')
    }),
  ('disponibilidad', {
    'fields':('status', 'devolucion')
  })
  )
  pass