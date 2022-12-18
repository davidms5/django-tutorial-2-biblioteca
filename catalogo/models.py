from django.db import models
from django.urls import reverse
import uuid
# Create your models here. 

class idiomas(models.Model):
  idioma = models.CharField(max_length=200)

  def __str__(self):
    return self.idioma
    
  class Meta:
    verbose_name_plural = 'idiomas'
    

class genero(models.Model):
    nombre = models.CharField(max_length = 200, help_text="inserte un genero") 

    def __str__(self):
       return self.nombre 

class libro(models.Model):
    titulo = models.CharField(max_length = 200)

    idioma = models.ForeignKey('idiomas', on_delete=models.SET_NULL,null=True)

    autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)
  
    sinopsis = models.TextField(max_length=1000, help_text='ingrese una breve sinopsis')

    isbn = models.CharField('ISBN', max_length=13, help_text='13 Caracteres <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    genero= models.ManyToManyField(genero, help_text= "seleccione un genero para este libro")

    def __str__(self):
      return self.titulo

    def get_absolute_url(self):
      return reverse('libro-detalles', args=[str(self.id)])
      
    def display_genero(self):
      """
      Creates a string for the Genre. This is required to display genre in Admin.
      """
      return ', '.join([ genero.nombre for genero in self.genero.all() ])
    display_genero.short_description = 'Generos del libro'


class libroInstance(models.Model): 

    id= models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='ID único para este libro particular en toda la biblioteca')

    libro = models.ForeignKey('libro', on_delete= models.SET_NULL, null=True)

    impreso = models.CharField(max_length=200) 

    devolucion = models.DateField(null=True, blank=True)


    LOAN_STATUS =  (
      ('m', 'Maintenance'),
      ('o', 'On loan'),
      ('a', 'Available'),
      ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Disponibilidad del libro') 

    class Meta:
      ordering = ["devolucion"]

    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        return f'{self.id} ({self.libro.titulo})' 

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    agno_nacimiento = models.DateField('año nacimiento', null=True, blank=True)
    fallecimiento = models.DateField('fallecimiento', null=True, blank=True) 

    def get_absolute_url(self):
      """
        Retorna la url para acceder a una instancia particular de un autor.
        """
      return reverse('detalle_autor', args=[str(self.id)])

    class Meta:
      verbose_name_plural = 'autor'
    def __str__(self):
      """
        String para representar el Objeto Modelo
        """
      return '%s, %s' % (self.apellido, self.nombre)
