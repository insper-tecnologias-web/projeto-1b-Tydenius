from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/<int:id>', views.index_update, name='index_update'),
    path('delete/<int:id>', views.index_delete, name='index_delete'),
    path('tags/listar', views.listarTags, name='listar_Tags'),
    path('tags/listar/<int:id>', views.listarNoteTag, name='listar_Note_Tag')
]