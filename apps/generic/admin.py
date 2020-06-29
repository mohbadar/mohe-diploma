from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Contact, UserFacultyRelation, University, Faculty, Department, BlankDiploma, Certificate, UniversityDiplomaDistribution



# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class UserFacultyRelationInline(admin.StackedInline):
    model = Faculty
    can_delete = False
    verbose_name_plural = 'faculty'

class UserUniversityRelationInline(admin.StackedInline):
    model = University
    can_delete = False
    verbose_name_plural = 'university'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserFacultyRelationInline,UserUniversityRelationInline)



# Register your models here.
admin.site.register(UniversityDiplomaDistribution)
admin.site.register(BlankDiploma)
admin.site.register(Certificate)
admin.site.register(Contact)
admin.site.register(UserFacultyRelation)
admin.site.register(University)
admin.site.register(Faculty)
admin.site.register(Department)
