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



UNIVERSITIES = (
    ("Kabul University", "KU"),
    ("Herat University", "HU")
)


class Degree(models.Model):
    firstname = models.CharField(name="firstname", max_length=255, unique=True, db_index=True,help_text="First Name")
    lastname = models.CharField(name="lastname", max_length=255, unique=True, db_index=True,help_text="Last Name")
    dob = models.DateField(name="dob", max_length=255, unique=True, db_index=True,help_text="Date of Birth")
    department = models.CharField(name="department", max_length=255, unique=True, db_index=True,help_text="Department")
    faculty = models.CharField(name="faculty", max_length=255, unique=True, db_index=True,help_text="Faculty")
    university = models.CharField(name="university", max_length=255, unique=True, db_index=True,help_text="University")
    graduation_year = models.IntegerField(name="graduation_year", unique=True, db_index=True,help_text="Graduation Year")
    slug = models.SlugField(max_length = 250, null = True, blank = True, editable=False)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    student_image = models.ImageField(name="student_image", null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.firstname)
        super(Degree, self).save(*args, **kwargs) # Call the real save() method

    def __str__(self):
        return self.firstname + " - "  + self.lastname +  " - "+ self.university + " - "+ self.faculty + " - "+ self.department 
    class Meta:
        ordering = ['-created_at']
        permissions = (
            ("can_register_certificate", "Can Register a New Certificate"),
            ("can_view_ownfaculty_certificates", "Can View Own Faculty Certificate")
        )
