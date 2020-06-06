from django.contrib import admin

from .models import Tenant,Template

# Register your models here.
admin.site.register(Tenant)
admin.site.register(Template)