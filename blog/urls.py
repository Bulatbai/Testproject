from django.urls import path

 
from  . import views
 
urlpatterns = [
    path('', views.Index, name='main'),
    path('upload/', views.image_upload_view),
    path('blogi/', views.Blogi, name='search-element'),
    path('comments/', views.comm, name='comments'),
    path('blogi/<int:id>/', views.detail_post, name='place'),
    path('blogi/<int:id>/edit/', views.edit_place, name='edit-place'),
    path('<int:id>/delete/', views.delete_place, name='del_place' ),
    path('accounts/register/', views.RegisterView.as_view(), name="register"),
    path('accounts/login/', views.LoginView.as_view(), name="login"),
    path('accounts/profile/', views.ProfilePage.as_view(), name="profile"),
    path('logout/', views.logout_user, name="logout-login"),
    # path('search/', views.Search, name='search-element')   
    
]