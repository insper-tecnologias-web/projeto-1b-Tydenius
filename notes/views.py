from operator import methodcaller
from django.shortcuts import render, redirect,get_object_or_404
from .models import Note,Tag


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag = request.POST.get('tag')
        
        try:
                check = Tag.objects.only('id').get(name=tag).id
        except Tag.DoesNotExist:
                check = 0

        if check != 0:
                obj = Tag.objects.get(id=check)
                insert = Note(title=f'{title}', content= f'{content}', tag=obj )
                insert.save()

        else:
                insert = Tag(name=tag)
                insert.save()

                tag_id = Tag.objects.only('id').get(name=tag).id
                obj = Tag.objects.get(id=tag_id)

                insert = Note(title=f'{title}', content= f'{content}', tag=obj )
                insert.save()

            
            
        return redirect('index')
            
               
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})


def index_update(request, id):
   if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag = request.POST.get('tag')

        try:
                check = Tag.objects.only('id').get(name=tag).id
        except Tag.DoesNotExist:
                check = 0
        
        if check != 0:
                obj = Tag.objects.get(id=check)
                insert = Note(id=id, title=f'{title}', content= f'{content}', tag=obj )
                insert.save()
        else:
                insert = Tag(name=tag)
                insert.save()

                tag_id = Tag.objects.only('id').get(name=tag).id
                obj = Tag.objects.get(id=tag_id)

                insert = Note(id=id, title=f'{title}', content= f'{content}', tag=obj )
                insert.save()
                

        

        return redirect('index')

def index_delete(request, id):
   if request.method == 'POST':

            delete = Note.objects.get(id=id)
            delete.delete()

            return redirect('index')

                        