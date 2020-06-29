from django.contrib import admin
from .models import Form, Instance, Degree
# Register your models here.

class FormAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(Form)
admin.site.register(Instance)
admin.site.register(Degree)