from django.db import models
from django.contrib.postgres.fields import JSONField
# Create your models here.

class Tenant(models.Model):
    name = models.CharField(name="name", max_length=255, unique=True, db_index=True,help_text="Tenant Name")
    code = models.CharField(name="code", max_length=255, unique=True, db_index=True,help_text="Tenant Code")
    location = models.CharField(name="location", max_length=255, verbose_name="Location")
    active = models.BooleanField (name="active",default=True, verbose_name="Is Active?")
    brand = models.ImageField(verbose_name="Tenant Brand", name="tenant_brand")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.name + " ( " + self.code + " ) "
    


class Template(models.Model):
    name = models.CharField(name="name", max_length=255, unique=True, db_index=True,verbose_name="Template Name")
    tenant = models.ForeignKey(to=Tenant, on_delete="cascade")
    template = JSONField()
    active = models.BooleanField(name="active", verbose_name="Is Active", default=True)

    def __str__(self):
        return self.tenant.name +" - "+ self.name

