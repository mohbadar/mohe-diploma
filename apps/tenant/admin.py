from django.contrib import admin

from .models import Tenant,Template, Center

# Register your models here.
admin.site.register(Template)
admin.site.register(Center)
admin.site.register(Tenant)
