from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User, Group
from .models import Contact, UserFacultyRelation, University, Faculty, Department, BlankDiploma, Certificate, UniversityDiplomaDistribution


class CertificateAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def get_visible_users(self, request):  # small refactor to re-use in filter
        query_set = Group.objects.filter(user=request.user)
        group_list = []
        for g in query_set:
            group_list.append(g.name)
        # To get all users associated in those groups
        return User.objects.filter(groups__name__in=group_list)

    def get_queryset(self, request):
        users = self.get_visible_users(request)
        # Override the get_queryset method for Admin
        qs = super(CertificateAdmin, self).get_queryset(request)

        if not request.user.is_superuser:
            return qs.filter(user=request.user)
            # return qs.filter(user__in=users)
        else:
            return qs



# Define an inline admin descriptor for model
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
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Contact)
admin.site.register(UserFacultyRelation)
admin.site.register(University)
admin.site.register(Faculty)
admin.site.register(Department)
