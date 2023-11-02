from django.contrib import admin
from .models import Gender, Author, Photo

# Register your models here.

class GenderAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

class AuthorAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

class PhotoAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ('name', 'year', 'rating', 'detalle')
    list_filter = ('genders', 'Author', 'year')
    ordering = ('year',)

admin.site.register(Gender, GenderAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Photo, PhotoAdmin)