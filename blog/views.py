 
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.shortcuts import render,HttpResponse
from django.http import Http404
from .forms import ImageForm
from . import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(Blogi)
            # Get the current instance object to display in the template
        img_obj = form.instance
        return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form}) 





 

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





 




# def Search(request):
#     QueryValue = request.GET.get('q', '')
#     if QueryValue:
#         post = models.Image.objects.filter(title__icontains=QueryValue)
#     else:
#         post = models.Image.objects.all()
#     return render(request, 'basesmy.html', {'post': post})


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
  



class RegisterView(TemplateView):
    template_name = "registration/register.html"

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            if password == password2:
                User.objects.create_user(username, email, password)
                return redirect(reverse("login"))

        return render(request, self.template_name) 

class LoginView(TemplateView):
    template_name = "registration/login.html"

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("search-element")
            else:
                context['error'] = "Логин или пароль неправильные"
        return render(request, self.template_name, context)


class ProfilePage(TemplateView):
    template_name = "registration/profile.html"


def logout_user(request):
    logout(request)
    return redirect('login')