from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('profiles', views.profiles, name='profiles'),
    path('profile/<str:pk>', views.profile_page, name='profile'),
    path('createform', views.createform, name='createform'),
    path('update/<str:pk>', views.update_form, name='update'),
    path('delete/<str:pk>', views.delete_room, name='delete'),
    path('signin', views.signin_form, name='signin'),
    path('signout', views.signout, name='signout'),
]