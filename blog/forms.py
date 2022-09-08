from django import forms
from .models import Image

 
 
from .models import  Image
 
from django.contrib.auth.models import User

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image','description', 'amount_p','price' )


