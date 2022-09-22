 
import imp
from tkinter.messagebox import RETRY
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.shortcuts import render,HttpResponse, get_object_or_404
from django.http import Http404
from .forms import ImageForm, CommentForm
from . import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.generic import TemplateView 
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .models import   Comment, Image
from django.views.generic.detail import    DetailView







def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(Blogi)
            # Get the current instance object to display in the template
        img_obj = form.instance
        return render(request, 'fruitkha/create_post.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'fruitkha/create_post.html', {'form': form}) 





def Index(request):
    return render(request, 'fruitkha/Home.html' )



def Insruction(request):
    return render(request, 'fruitkha/index.html' )



def Cart(request):
    return render(request, 'fruitkha/cart.html' )




def edit_place(request, id):
    place_edit = models.Image.objects.get(id=id)
    if request.method == 'POST':
        place_form = ImageForm(data=request.POST, instance=place_edit)
        if place_form.is_valid():
            place_form.save()
            return redirect(detail_post, id=id)
    place_forms = ImageForm(instance=place_edit)
    return  render(request, 'fruitkha/create_post.html', {'form': place_forms})


def delete_place(request, id):
    place_delete = models.Image.objects.get(id=id)
    place_delete.delete()
    return redirect(Blogi)





 




# class PostDetailView(TemplateView):
#     model = Comment
#     template_name = 'registration/koments.html'
def comm(request, id):
    post = models.Comment.objects.get(id=id)
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid:
            comment = comment_form.save(commit=False)
            comment.save()
        else:
            return HttpResponse('<h1> ERROR</h1>')
    else:
        comment_form = CommentForm()
    return render(request, 'registration/koments.html' , {'comment_form': comment_form,'comments': post})







def Blogi(request):
    QueryValue = request.GET.get('q')
    if QueryValue:
        post = models.Image.objects.filter(title__icontains=QueryValue)
        
    else:
        post = models.Image.objects.all()
        number = 0
 
    paginator = Paginator(post, 3) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
 
    
    return render(request, 'fruitkha/shops.html', {'post': page_obj })
                                                 



class RegisterView(TemplateView):
    template_name = "fruitkha/regist.html"

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')
            user = authenticate(request, username=username, password=password, email=email)
            if user is not None:
                context['error'] = 'user aurhenticated'
            else:
               if password == password2:
                  User.objects.create_user(username, email, password)
                  return redirect(reverse("login"))
        
        return render(request, self.template_name, context) 






class LoginView(TemplateView):
    template_name = "fruitkha/login.html"

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("search-element")
            
            context['error'] = "Логин или пароль неправильные"
        return render(request, self.template_name, context)

class ProfilePage(TemplateView):
    template_name = "registration/profile.html"


def logout_user(request):
    logout(request)
    return redirect('login')





def detail_post(request, id):
    post = models.Image.objects.all()
    # post = 
    try:
        ost = models.Image.objects.get(id=id)
   
        try:
            comment =  {}
             
        except models.Image.DoesNotExist:
            return HttpResponse('<h1>No Comments</h1>')
    except models.Image.DoesNotExist:
        # raise Http404('Post does not exixst, baby')
        return  HttpResponse('<h1> 404 Page not found </h1>')
    return render(request, 'fruitkha/single-product.html' , { 
                                          'postingo': ost,})

 



def detail(request):
    

    # posti = get_object_or_404(Image, slug=post)
    posts = models.Comment.objects.filter(active=True)
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid:
            comment = comment_form.save(commit=False)
            comment.save()
        else:
            return HttpResponse('<h1> ERROR</h1>')
    else:
        comment_form = CommentForm()
    return render(request, 'basesmy.html' , {'comment_form': comment_form,'comments': posts,})
                                           
 


  
