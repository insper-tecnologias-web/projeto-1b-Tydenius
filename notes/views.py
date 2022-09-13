from operator import methodcaller
from django.shortcuts import render, redirect,get_object_or_404
from .models import Note


def index(request):
    if request.method == 'POST':
            title = request.POST.get('titulo')
            content = request.POST.get('detalhes')

            insert = Note(title=f'{title}', content= f'{content}' )
            insert.save()

            return redirect('index')
            
               
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})


def index_update(request, id):
   if request.method == 'POST':
            title = request.POST.get('titulo')
            content = request.POST.get('detalhes')

            insert = Note(id=id, title=f'{title}', content= f'{content}' )
            insert.save()

            return redirect('index')

def index_delete(request, id):
   if request.method == 'POST':

            delete = Note.objects.get(id=id)
            delete.delete()

            return redirect('index')

                        