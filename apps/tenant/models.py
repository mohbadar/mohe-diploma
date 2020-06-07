from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.

class Tenant(models.Model):
    name = models.CharField(name="name", max_length=255, unique=True, db_index=True,help_text="Tenant Name")
    code = models.CharField(name="code", max_length=255, unique=True, db_index=True,help_text="Tenant Code")
    location = models.CharField(name="location", max_length=255, verbose_name="Location")
    active = models.BooleanField (name="active",default=True, verbose_name="Is Active?")
    brand = models.ImageField(verbose_name="Tenant Brand", name="tenant_brand")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=1,to_field="id")
    def __str__(self):
        return self.name + " ( " + self.code + " ) "
    



class Template(models.Model):
    name = models.CharField(name="name", max_length=255, unique=True, db_index=True,verbose_name="Template Name")
    tenant = models.ForeignKey(to=Tenant, on_delete=models.CASCADE, default=1,to_field="id")
    template =  models.TextField(name="template", max_length=2500, unique=True, db_index=True,help_text="JSON")
    active = models.BooleanField(name="active", verbose_name="Is Active", default=True)

    def __str__(self):
        return self.tenant.name +" - "+ self.name


class Center(models.Model):
    name = models.CharField(name="name", max_length=255, unique=True, db_index=True,help_text="Center Name")
    code = models.CharField(name="code", max_length=255, unique=True, db_index=True,help_text="Center Code")
    latest_appointment = models.DateTimeField(name="latest_appointment", verbose_name="Latest Appointment Date", blank=True, null=True)
    appointments = models.TextField(name="appointments", verbose_name="Appointments", editable=False, default=None, blank=True, null=True)
    country = models.CharField(name="country", max_length=255,help_text="Country", blank=True, null=True)
    province = models.CharField(name="province", max_length=255,help_text="Province", blank=True, null=True)
    town = models.CharField(name="town", max_length=255, help_text="Town", blank=True, null=True)
    village = models.CharField(name="village", max_length=255,help_text="Village", blank=True, null=True)
    latitude = models.FloatField(name="latitude", default=0.0000, verbose_name="Center GIS Latitude", blank=True, null=True)
    longtitude = models.FloatField(name="longtitude", default=0.0000, verbose_name="Center GIS Longtitude", blank=True, null=True)
    active = models.BooleanField (name="active",default=True, verbose_name="Is Active?")
    tenant = models.ForeignKey( to= Tenant, on_delete=models.CASCADE, default=1,to_field="id")
    template = models.ForeignKey( to= Template, on_delete=models.CASCADE, default=1,to_field="id")
    def __str__(self):
        return self.tenant.name + " - " +self.name + " ( " + self.code + " ) "
    