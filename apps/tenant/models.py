from django.db import models

# Create your models here.

class Tenant(models.Model):
    name = models.CharField(name="name", max_length=255, unique=True, db_index=True,help_text="Tenant Name")
    code = models.CharField(name="code", max_length=255, unique=True, db_index=True,help_text="Tenant Code")
    location = models.CharField(name="location", max_length=255, verbose_name="Location")
    active = models.BooleanField (name="active",default=True, verbose_name="Is Active?")
    brand = models.ImageField(verbose_name="Tenant Brand", name="tenant_brand")
    def __str__(self):
        return self.name + " ( " + self.code + " ) "
    

class Office(models.Model):
    name = models.CharField(name="name",verbose_name="Office Name", unique=True, db_index=True,max_length=255 )
    code = models.CharField(name="code", max_length=255, unique=True, db_index=True,verbose_name="Office Code")
    tenant = models.ForeignKey(to=Tenant, on_delete="cascade")
    location = models.CharField(name="location", max_length=255, unique=True, db_index=True,verbose_name="Location")
    active = models.BooleanField(name="active", verbose_name="Is Active", default=True)

    def __str__(self):
        return self.tenant.name +" - "+ self.name +" - "+ self.code


class Template(models.Model):
    name = models.CharField(name="name", max_length=255, unique=True, db_index=True,verbose_name="Office Name")
    office = models.ForeignKey(to=Office, on_delete="cascade")
    template = models.TextField(name="template",verbose_name="Template JSON")
    active = models.BooleanField(name="active", verbose_name="Is Active", default=True)

    def __str__(self):
        return self.office.name +" - "+ self.name

