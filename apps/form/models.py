from django.db import models
from ..tenant.models import Tenant, Center
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
import datetime
# from django.contrib.postgres.fields import JSONField

# Create your models here.

class Form(models.Model):
    name = models.CharField(name="name", max_length=255, unique=True, db_index=True,help_text="Form Name")
    code = models.CharField(name="code", max_length=255, unique=True, db_index=True,help_text="Form Code")
    workflow  = models.TextField(name="workflow", max_length=2500, unique=True, db_index=True,help_text="JSON")
    structure =  models.TextField(name="structure", max_length=2500, unique=True, db_index=True,help_text="JSON")
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    slug = models.SlugField(max_length = 250, null = True, blank = True, editable=False) 
    tenant = models.ForeignKey(to= Tenant, on_delete= models.CASCADE,to_field="id" )
    center = models.ForeignKey(to=Center, on_delete=models.CASCADE, default=1,to_field="id")
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Form, self).save(*args, **kwargs) # Call the real save() method

    def __str__(self):
        return self.name + " - "  + self.code +  " - "+ self.tenant.name
	
    class Meta:
        ordering = ['-created_at']


class Instance(models.Model):
    form = models.ForeignKey(to = Form, on_delete=models.CASCADE, parent_link=True, related_name="form_instance_relationship", to_field="id")
    name = models.CharField(name="name", max_length=255, unique=True, db_index=True,help_text="Instance Name")
    data = models.TextField(name="data", max_length=2500, unique=True, db_index=True,help_text="Data")
    workflow_status = models.CharField(name="workflow_status", max_length=255, unique=True, db_index=True,help_text="Workflow Status")
    tenant = models.ForeignKey(to= Tenant, on_delete= models.CASCADE,to_field="id" )
    center = models.ForeignKey(to=Center, on_delete=models.CASCADE, default=1,to_field="id")
    instance_no = models.CharField(max_length=500, null=True, blank=True, editable=False)
    
    def save(self, *args, **kwargs):
        last_instance = Instance.objects.all().order_by('id').last()
        if not last_instance:
            self.instance_no =  'ASR' + str(datetime.date.today().year) +"01"
        else:
            instance_no = last_instance.instance_no
            instance_int = int(instance_no.split('ASR')[-1])
            new_instance_int = instance_int + 1
            new_instance_no = 'ASR' + str(new_instance_int)
            self.instance_no = new_instance_no

        super(Instance, self).save(*args, **kwargs) # Call the real save() method


    def __str__(self):
        return self.tenant.name + " - " + self.form.name + " - "+ self.name + " - "+ self.workflow_status + " - "+ self.instance_no

