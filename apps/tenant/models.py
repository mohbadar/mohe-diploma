from django.db import models

# Create your models here.

class Tenant(models.Model):
    name = models.CharField(name="name", max_length=255, unique=True, db_index=True,help_text="Tenant Name")
    code = models.CharField(name="code", max_length=255, unique=True, db_index=True,help_text="Tenant Code")
    active = models.BooleanField (name="active",default=True, verbose_name="Is Active?")

    def __str__(self):
        return self.name + " ( " + self.code + " ) "
    