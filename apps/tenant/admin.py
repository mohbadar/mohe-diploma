from django.contrib import admin

from .models import Tenant, Office,Template

# Register your models here.
admin.site.register(Tenant)
admin.site.register(Office)
admin.site.register(Template)