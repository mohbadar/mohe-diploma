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


class Instance (models.Model):
    form = models.ForeignKey(to = Form, on_delete="cascade", parent_link=True, related_name="form_instance_relationship", to_field="id")
    name = models.CharField(name="name", max_length=255, unique=True, db_index=True,help_text="Instance Name")
    data = models.TextField(name="data", max_length=2500, unique=True, db_index=True,help_text="Data")
    workflow_status = models.CharField(name="workflow_status", max_length=255, unique=True, db_index=True,help_text="Workflow Status")
    tenant = models.ForeignKey(to= Tenant, on_delete= "cascade",to_field="id" )

    def __str__(self):
        return self.tenant.name + " - " + self.form.name + " - "+ self.name + " - "+ self.workflow_status
    