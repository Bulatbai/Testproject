from django.db import models

from django.contrib.auth.models import User

class Image(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL,
                null=True, blank=True
                )
    amount_p = models.IntegerField(default=0)
    # location = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=50,  decimal_places=2, default=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    location = models.CharField(max_length=100 , null=True, blank=True, )
    def __str__(self):
        return self.title
        