from msilib.schema import ListView
from multiprocessing import context
from pyexpat import model
from turtle import title
from urllib import request
from winreg import QueryValue
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.shortcuts import render,HttpResponse
from django.http import Http404
from .forms import ImageForm
from . import models
from django.views.generic import ListView



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






# def Blogi(request):
#     user = models.Image.objects.all()
#     return render(request, 'proverka.html', {'post': user})
   

def detail_post(request, id):
    # user_ob = Post.objects.all()
    # user_obl = models.Image.objects.all()
    # if request.method == "POST":
    #     comment_person = Coment_Form(request.POST)
    #     if comment_person.is_valid():
    #         comment_person.save()
    #         return redirect(detail_post, id)
    # commet = Coment_Form() 
    
    try:
        # post = models.Post.objects.get(id=id)
        ost = models.Image.objects.get(id=id)
        try:
            comment =  {}
             
        except models.Model_Register.DoesNotExist:
            return HttpResponse('No Comments')
    except models.Image.DoesNotExist:
        raise Http404('Post does not exixst, baby')

    return render(request, 'watch.html', {'postingo': ost, 'com': comment})





def edit_place(request, id):
    place_edit = models.Image.objects.get(id=id)
    if request.method == 'POST':
        place_form = ImageForm(data=request.POST, instance=place_edit)
        if place_form.is_valid():
            place_form.save()
            return redirect(detail_post, id=id)
    place_forms = ImageForm(instance=place_edit)
    return  render(request, 'index.html', {'form': place_forms})


def delete_place(request, id):
    place_delete = models.Image.objects.get(id=id)
    place_delete.delete()
    return redirect(Blogi)





 




def Search(request):
    QueryValue = request.GET.get('q', '')
    if QueryValue:
        post = models.Image.objects.filter(title__icontains=QueryValue)
    else:
        post = models.Image.objects.all()
    return render(request, 'basesmy.html', {'post': post})


# class Search(ListView):
#     template_name = 'proverka.html'
#     context_object_name = 'product'
#     paginate_by = 1
 
#     def get_queryset(self):    
#           return  models.Image.objects.filter(title__icontains=self.request.GET.get('q'))

#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['q'] = self.request.GET.get('q')
#         return context
 

def Blogi(request):
    QueryValue = request.GET.get('q')
    if QueryValue:
        post = models.Image.objects.filter(title__icontains=QueryValue)
    else:
        post = models.Image.objects.all()
   

    # contact_list = models.Image.objects.all()
    paginator = Paginator(post, 3) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'proverka.html', {'post': page_obj})
  



