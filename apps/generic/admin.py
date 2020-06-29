from django.contrib import admin

from .models import Contact, UserFacultyRelation, University, Faculty, Department

# Register your models here.
admin.site.register(Contact)
admin.site.register(UserFacultyRelation)
admin.site.register(University)
admin.site.register(Faculty)
admin.site.register(Department)