from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages

from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView

from .models import Photo, Author
from .forms import PhotoForm, UsuariosForm


# Home
class HomeView(TemplateView):
    template_name = 'Photoapp/home.html'

# About us
class Aboutus(TemplateView):
    template_name = 'Photoapp/aboutus.html'

# Contact
class Contact(TemplateView):
    template_name = 'Photoapp/contact.html'

# Lista de Fotos
class PhotoList(ListView):
    model = Photo

# Lista de Fotógrafos
class AuthorList(ListView):
    model = Author

# Agregar Fotos
class PhotoCreate(CreateView):
    model = Photo
    form_class = PhotoForm
    success_url = reverse_lazy('photos')

# Editar Fotos
class PhotoUpdate(UpdateView):
    model = Photo
    form_class = PhotoForm
    template_name_suffix = "_update_form" 

    def get_success_url(self):
        return reverse_lazy('photos-editar', args=[self.object.id])+"?ok"

# Eliminar Fotos
class PhotoDelete(DeleteView):
    model = Photo
    success_url = reverse_lazy('photos')

# Login y Logout
class UpLoginView(LoginView):
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('home')
    
    def form_invalid(self, form):
        messages.error(self.request, "Usuario o contraseña inválidos")
        return self.render_to_response(self.get_context_data(form=form))

# Registro de usuarios
def usuario(request):
    if request.method == 'POST':
        miForm = UsuariosForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            
            miForm.save()
            return render(request, "Photoapp/home.html/")
    else:    
        miForm = UsuariosForm()

    return render(request, "Photoapp/usuario.html/", {"form": miForm})
