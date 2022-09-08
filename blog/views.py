from django.shortcuts import render

from django.shortcuts import render
from .forms import ImageForm
from . import models

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form}) 


def Blogi(request):
    user = models.Image.objects.all()
    return render(request, 'proverka.html', {'post': user})
