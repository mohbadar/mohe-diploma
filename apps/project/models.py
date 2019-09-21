from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor_uploader.fields import  RichTextUploadingField
from django.utils.text import slugify

# Create your models here.

# category model class
class ProjectCategory(models.Model):
	name = models.CharField(max_length=128, verbose_name=('Category Name'), unique=True)
	created_at = models.DateTimeField(default=timezone.now, editable=False)


	def __str__(self):
		return '{}: {}'.format(self.created_at.strftime('%Y-%m-%d'), self.name)

	class Meta:
		ordering = ['-created_at']

class Project(models.Model):
	category = models.ForeignKey(ProjectCategory, related_name='project_category' , on_delete='cascade')
	created_at = models.DateTimeField(default=timezone.now, editable=False)
	title = models.CharField(max_length=512, unique=True)
	abstract = models.TextField()
	slug = models.SlugField(max_length = 250, null = False, blank = False, editable=False, unique=True)
	content = RichTextUploadingField()

	def save(self, *args, **kwargs):	   
	   self.slug = slugify(self.title)
	   super(Project, self).save(*args, **kwargs) # Call the real save() method
	
	def __str__(self):
		return '{}: {}'.format(self.created_at.strftime('%Y-%m-%d'), self.title)

	class Meta:
		ordering = ['-created_at']


