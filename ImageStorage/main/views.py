import os
from django.shortcuts import render
from .models import Images
from .forms import AddImageForm
from django.shortcuts import redirect


def index(request):
    images = Images.objects.all()
    return render(request, 'main/index.html', {'images': images})

def uploadImage(request):
    if request.method == "POST":
        form = AddImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AddImageForm()
    return render(request, 'main/upload.html', {'form': form})

def deleteImage(request, pk):
    image = Images.objects.get(id=pk)
    if os.path.exists(image.image.path):
        os.remove(image.image.path)
    image.delete()
    return redirect('/')