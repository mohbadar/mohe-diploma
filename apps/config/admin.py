from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

class AdminTemplate(DjangoMpttAdmin):
    pass

admin.site.site_header = 'DFI Site Administration'
