from django.conf.urls import url, re_path

from . import views


urlpatterns = [
 re_path(r'^$', views.index, name='index'),
  re_path(r'^libros/$', views.BookListView.as_view(), name='libros'),
  re_path(r'^libro/(?P<pk>\d+)$', views.BookDetailView.as_view(), name = 'libro-detalles'),
  re_path(r'^autores/$', views.autorLista.as_view(), name='autores'),
  re_path(r'^autor/(?P<pk>\d+)$', views.autorDetalles.as_view(), name = 'detalle_autor'),
]