from django.db import models

# Create your models here.

class Organization(models.Model):
    name = models.CharField(name="name", max_length=255, unique=True, db_index=True,help_text="Organization Name")
    code = models.CharField(name="code", max_length=255, unique=True, db_index=True,help_text="Organization Code")