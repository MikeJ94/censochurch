from django.contrib import admin
from .models import Estado, Person, Hijo

""" Tabla Intermedia
    class HijoPersonInline(admin.TabularInline):
    model = HijoPerson
    extra = 1
    autocomplete_fields = ['hijo']

class HijoAdmin(admin.ModelAdmin):
    inlines = (HijoPersonInline,)
    search_fields = ('name'),
    ordering = ['name'] 
    Tabla Intermedia """

# Register your models here.
#admin.site.register(Person)

#admin.site.register(Hijo)
#admin.site.register(Estado)