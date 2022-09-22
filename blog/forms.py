from django import forms
from .models import Image, Comment

 
 
from .models import  Image
 
from django.contrib.auth.models import User

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('user','title','location', 'image','description', 'amount_p', 'price')




 
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')




