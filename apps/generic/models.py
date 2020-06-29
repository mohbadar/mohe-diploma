from django.db import models
from django.conf import settings
from ..tenant.models import Tenant
# Create your models here.

class Contact(models.Model):
    name = models.CharField(name="name",verbose_name="Name", unique=True, db_index=True,max_length=255 )
    email = models.EmailField(name="email", max_length=255, unique=True, db_index=True,verbose_name="Email")
    phone = models.CharField(name="phone", max_length=13, unique=True, db_index=True,verbose_name="Phone")
    tenant = models.ForeignKey(to=Tenant, on_delete=models.CASCADE, blank=True, null=True, default=1)
    message = models.TextField(name="message",verbose_name="Message")

    def __str__(self):
        return self.name +" - "+ self.email +" - "+ self.message

class University(models.Model):
    name = models.CharField(name="name",verbose_name="Name", unique=True, db_index=True,max_length=255 )
    code = models.CharField(name="code",verbose_name="code", unique=True, db_index=True,max_length=255 )
    phone = models.CharField(name="phone", max_length=13, unique=True, db_index=True,verbose_name="Phone")

    def __str__(self):
        return self.name +" - "+ self.code 


class Faculty(models.Model):
    name = models.CharField(name="name",verbose_name="Name", unique=True, db_index=True,max_length=255 )
    code = models.CharField(name="code",verbose_name="code", unique=True, db_index=True,max_length=255 )
    phone = models.CharField(name="phone", max_length=13, unique=True, db_index=True,verbose_name="Phone")
    university = models.ForeignKey(to=University, on_delete=models.CASCADE, blank=True, null=True, default=1)

    def __str__(self):
        return self.university.name +" - "+ self.name +" - "+ self.code


class Department(models.Model):
    name = models.CharField(name="name",verbose_name="Name", unique=True, db_index=True,max_length=255 )
    code = models.CharField(name="code",verbose_name="code", unique=True, db_index=True,max_length=255 )
    faculty = models.ForeignKey(to=Faculty, on_delete=models.CASCADE, blank=True, null=True, default=1)

    def __str__(self):
        return self.university.name +" - "+ self.faculty.name +" - "+ self.name + " - " + self.code


class Cycle(models.Model):
    name = models.CharField(name="name",verbose_name="Name", unique=True, db_index=True,max_length=255 )
    code = models.CharField(name="code",verbose_name="code", unique=True, db_index=True,max_length=255 )
    date = models.DateField(name="date", auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.name + " - " + self.code


class Diploma(models.Model):
    number = models.CharField(name="number",verbose_name="Number", unique=True, db_index=True,max_length=255 )
    university = models.ForeignKey(to=University, on_delete=models.CASCADE, blank=True, null=True, default=1)

    def __str__(self):
        return self.university.name +" - "+ self.faculty.name +" - "+ self.name + " - " + self.code


class UserFacultyRelation(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    faculty = models.OneToOneField(Faculty,
        on_delete=models.CASCADE,
        related_name='faculty',
    )