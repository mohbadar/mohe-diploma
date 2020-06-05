from django.db import models

from ..tenant.models import Tenant
# Create your models here.

class Form(models.Model):
    name = models.CharField(name="name", max_length=255, unique=True, db_index=True,help_text="Form Name")
    code = models.CharField(name="code", max_length=255, unique=True, db_index=True,help_text="Form Code")
    workflow = models.TextField(name="worflow", max_length=255, unique=True, db_index=True,help_text="Form Workflow Json Field")
    structure = models.TextField(name="structure", max_length=255, unique=True, db_index=True,help_text="Form Structure Json Field")
    tenant = models.ForeignKey(to= Tenant, on_delete= "cascade",to_field="id" )

    def __str__(self):
        return self.name + " - " + self.code + " - "+ self.tenant.name
    