from django.urls import path
from  . import views
urlpatterns = [
     
    path('upload/', views.image_upload_view),
    path('blogi/', views.Blogi, name='blog')
    
]