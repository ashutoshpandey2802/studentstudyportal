from django.shortcuts import render,redirect
from . forms import *
from django.http import HttpResponse
from django.contrib import messages
from django.views import generic



# Create your views here.


def home(request):
    return render(request,'dashboard/home.html')


def notes(request):
    if request.method=="POST":
        form=NotesForms(request.POST)
        if form.is_valid():
            notes=Notes(user=request.user,title=request.POST['title'],description=request.POST['description'])
            notes.save()
        
        messages.success(request,f'notes addded from {request.user.username} succussfully')
    
    
    form=NotesForms()
    notes=Notes.objects.filter(user=request.user)
    context={'notes':notes,"form": form}
    return render(request,'dashboard/notes.html',context)


def delete_note(request,pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect("notes")


def NotesDetailView ( DetailView):
    model=Notes