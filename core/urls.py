from django.urls import path;
from . import views;
from .views import index;

# Se instancian los distintos / o views de la pagina

urlpatterns = [
    path('', views.index, name = 'index'),
    path('signup', views.signup, name = 'signup'),
    path('signin', views.signin, name = 'signin'),
    path('logout', views.logout, name = 'logout'),
    path('setting', views.settings, name = 'setting'),
    path('upload', views.upload, name = 'upload')


]