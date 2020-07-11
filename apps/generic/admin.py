from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User, Group
from .models import  UserFacultyRelation, University, Faculty, Department, BlankDiploma, Certificate, UniversityDiplomaDistribution
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django import forms
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect



def export_selected_objects(modeladmin, request, queryset):
    selected = queryset.values_list('pk', flat=True)
    ct = ContentType.objects.get_for_model(queryset.model)
    return HttpResponseRedirect('/export/?ct=%s&ids=%s' % (
        ct.pk,
        ','.join(str(pk) for pk in selected),
    ))

class UniversityAdmin(admin.ModelAdmin):
    search_fields = ('name', 'code')
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
        qs = super(UniversityAdmin, self).get_queryset(request)

        if not request.user.is_superuser:
            return qs.filter(user=request.user)
        else:
            return qs


class FacultyAdmin(admin.ModelAdmin):
    search_fields = ('name', 'code')
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
        qs = super(FacultyAdmin, self).get_queryset(request)

        if not request.user.is_superuser:
            # if request.user.has_perm('auth.view_user'):
            #     print(request.user.has_perm('auth.view_user'))
            return qs.filter(user=request.user)
        else:
            return qs


def departmentform_factory(faculty):
    class DepartmentForm(forms.ModelForm):
        m_file = forms.ModelChoiceField(
            queryset=Department.objects.filter(faculty=faculty)
        )
    return DepartmentForm


class DepartmentAdmin(admin.ModelAdmin):
    search_fields = ('name', 'code')
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def get_form(self, request, obj=None, **kwargs):
        if request.user.faculty is not None:
            kwargs['form'] = departmentform_factory(request.user.faculty)
        return super(DepartmentAdmin, self).get_form(request, obj, **kwargs)

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
        qs = super(DepartmentAdmin, self).get_queryset(request)

        if not request.user.is_superuser:
            print('We are hrere')
            # if request.user.has_perm('auth.view_user'):
            #     print(request.user.has_perm('auth.view_user'))
            return qs.filter(faculty=request.user.faculty)
        else:
            return qs

def make_print(modeladmin, request, queryset):
    print('query : ')
    # queryset.update(status='p')
make_print.short_description = "Print Selected Diplomas"

class CertificateAdmin(admin.ModelAdmin):
    search_fields = ('firstname', 'lastname','certificate_status')
    actions = [make_print]
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
            # if request.user.has_perm('auth.view_user'):
            #     print(request.user.has_perm('auth.view_user'))
            return qs.filter(user=request.user)
        else:
            return qs



class BlankDiplomaAdmin(admin.ModelAdmin):
    search_fields = ('barcode',)
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
        qs = super(BlankDiplomaAdmin, self).get_queryset(request)

        if not request.user.is_superuser:
            # if request.user.has_perm('auth.view_user'):
            #     print(request.user.has_perm('auth.view_user'))
            return qs.filter(user=request.user)
        else:
            return qs


class UniversityDiplomaDistributionAdmin(admin.ModelAdmin):
    search_fields = ('name', 'code')
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
        qs = super(UniversityDiplomaDistributionAdmin, self).get_queryset(request)

        if not request.user.is_superuser:
            if request.user.has_perm('auth.view_user'):
                print(request.user.has_perm('auth.view_user'))
            return qs.filter(user=request.user)
        else:
            return qs

# Define an inline admin descriptor for model
class UserFacultyRelationInline(admin.StackedInline):
    model = UserFacultyRelation
    can_delete = False
    verbose_name_plural = 'faculty'


class UserUniversityRelationInline(admin.StackedInline):
    model = University
    can_delete = False
    verbose_name_plural = 'university'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserFacultyRelationInline,)



# Register your models here.
admin.site.register(UniversityDiplomaDistribution, UniversityDiplomaDistributionAdmin)
admin.site.register(BlankDiploma, BlankDiplomaAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(UserFacultyRelation)
admin.site.register(University, UniversityAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Department, DepartmentAdmin)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.add_action(export_selected_objects, 'export_selected')