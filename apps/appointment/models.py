from django.db import models
from ..tenant.models import Center, Template, Tenant
from ..form.models import Instance

# Create your models here.


class Appointment(models.Model):
    center = models.ForeignKey( to= Center, on_delete=models.CASCADE, default=1,to_field="id")
    queue_no = models.IntegerField(name="queue_no", verbose_name="Queue Number", default=0)
    appointment_date = models.DateField(name="appointment_date", verbose_name="Appointment Date", null=True, blank=True)
    start_time = models.CharField(name="start_time", max_length=255,verbose_name="Start Time", )
    end_time = models.CharField(name="end_time", max_length=255 , verbose_name="End Time",)
    instance = models.ForeignKey(to=Instance, on_delete=models.CASCADE, default=0)
    def __str__(self):
        return self.center.name + " - " +self.queue_no + " ( " + self.start_time +" - "+ self.end_time + " ) "