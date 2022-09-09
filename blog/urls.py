from django.urls import path
from  . import views
urlpatterns = [
     
    path('upload/', views.image_upload_view),
    path('blogi/', views.Blogi, name='blog'),
    path('blogi/<int:id>/', views.detail_post, name='place'),
    path('blogi/<int:id>/edit/', views.edit_place, name='edit-place'),
    path('<int:id>/delete/', views.delete_place, name='del_place' ),
]