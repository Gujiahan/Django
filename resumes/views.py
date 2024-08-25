from django.shortcuts import render,get_object_or_404,redirect
from .models import Archive
from .forms import ArchiveForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = ArchiveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resumes:index')
        else:
            return render(request, 'resumes/new.html', {'form': form})
    archive = Archive.objects.all()
    return render(request, 'resumes/index.html', {'archive': archive})


def new(request):
    form = ArchiveForm()
    return render(request, 'resumes/new.html', {'form': form})


def show(request,id):
    archive = get_object_or_404(Archive, id=id)
    if request.method == 'POST':
        form = ArchiveForm(request.POST, instance=archive)
        if form.is_valid():
            form.save()
            return redirect('resumes:show', archive.id)
        else:
            return render(request, 'resumes/edit.html', {'form': form, 'archive': archive})
    return render(request, 'resumes/show.html', {'archive': archive})

def edit(request,id):
    archive = get_object_or_404(Archive, id=id)
    form = ArchiveForm(instance=archive)
    return render(request, 'resumes/edit.html', {'form': form, 'archive': archive})

def delete(request,id):
    archive = get_object_or_404(Archive, id=id)
    archive.delete()
    return redirect('resumes:index')
