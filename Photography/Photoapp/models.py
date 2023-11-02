from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#Generos de fotos

class Gender(models.Model): 
    name = models.CharField(verbose_name="Género", max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Género"
        verbose_name_plural = "Géneros"
    
    def __str__(self):
        return self.name
    
#Fotógrafos

class Author(models.Model): 
    name = models.CharField(verbose_name="Fotógrafo", max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Fotógrafo"
        verbose_name_plural = "Fotógrafos"
    
    def __str__(self):
        return self.name
    
# Fotografía

class Photo(models.Model): 
    name = models.CharField(verbose_name="Fotografía", max_length=100)
    description = models.TextField(verbose_name="Detalle")
    RATING = [
        (1, "Pricipiante"),
        (2, "Intermedio"),
        (3, "Avanzado"),
        (4, "Experto"),
        (5, "Profesional"),
    ]

    rating = models.PositiveSmallIntegerField(choices=RATING)
    genders = models.ManyToManyField(Gender, verbose_name="Géneros")
    Author = models.ForeignKey(Author, verbose_name="Fotógrafo", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="Photo", null=True, blank=True, verbose_name="Imagen")
    year = models.SmallIntegerField(verbose_name="Año de captura", null=False, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Fotografía"
        verbose_name_plural = "Fotografías"
    
    def __str__(self):
        return self.name
    
    @admin.display(ordering="description")
    def detalle(self):
        return format_html(self.description[:150]+"...")