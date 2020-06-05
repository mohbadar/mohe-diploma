from django.db import models
from ..tenant.models import Tenant
# Create your models here.

class Contact(models.Model):
    name = models.CharField(name="name",verbose_name="Name", unique=True, db_index=True,max_length=255 )
    email = models.EmailField(name="email", max_length=255, unique=True, db_index=True,verbose_name="Email")
    phone = models.CharField(name="phone", max_length=13, unique=True, db_index=True,verbose_name="Phone")
    tenant = models.ForeignKey(to=Tenant, on_delete="cascade", blank=True)
    message = models.TextField(name="message",verbose_name="Message")

    def __str__(self):
        return self.name +" - "+ self.email +" - "+ self.message
