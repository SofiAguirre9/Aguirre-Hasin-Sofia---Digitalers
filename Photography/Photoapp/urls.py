from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('aboutus.html/', Aboutus.as_view(), name="aboutus"),
    path('contact.html/', Contact.as_view(), name="contact"),
    path('usuario.html/', usuario, name="usuario"),
    
    path('photos/', PhotoList.as_view(), name="photos"),
    path('author/', AuthorList.as_view(), name="author"),
   
    path('photos_agregar/', PhotoCreate.as_view(), name="photos-agregar"),
    path('photos_editar/<int:pk>/', PhotoUpdate.as_view(), name="photos-editar"),
    path('photos_eliminar/<int:pk>/', PhotoDelete.as_view(), name="photos-eliminar"),
    
    path('login/', UpLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="login"), name="logout"),
   
]
