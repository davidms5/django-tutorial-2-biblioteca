from django.shortcuts import render
from django.views import generic

from .models import idiomas, genero, libro, libroInstance, Autor

# Create your views here.
class BookListView(generic.ListView):
  model = libro
  paginate_by = 2
  #paginate_by hace que la view solo cargue la cantidad de registros que se le indique (en este caso 5)
class autorDetalles(generic.DetailView):
  model = Autor

class autorLista(generic.ListView):
  model = Autor
  
def index(request):
  numero_libros = libro.objects.all().count()
  instancias_libros = libroInstance.objects.all().count()
  instancias_disponibles = libroInstance.objects.filter(status__exact='a').count()

  numero_de_autores = Autor.objects.all().count()

  return render(request, 'index.html', context ={'libros':numero_libros,'instancias':instancias_libros,'instancias_disponibles':instancias_disponibles,'autores':numero_de_autores},)


class BookDetailView(generic.DetailView):
    model = libro