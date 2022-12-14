 
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Image(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL,
                null=True, blank=True
                )
    amount_p = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=50,  decimal_places=2, default=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True,)
    create_update = models.DateTimeField(auto_now=True, null=True, blank=True)
    location = models.CharField(max_length=100 , null=True, blank=True, )
    
    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey(Image, on_delete=models.SET_NULL, 
    related_name='comments', null=True, blank=True)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)