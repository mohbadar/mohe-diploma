from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor_uploader.fields import  RichTextUploadingField
from django.utils.text import slugify

# Create your models here.

# category model class
class PageCategory(models.Model):
	name = models.CharField(max_length=128, verbose_name=('Category Name'))
	created_at = models.DateTimeField(default=timezone.now, editable=False)


	def __str__(self):
		return '{}: {}'.format(self.created_at.strftime('%Y-%m-%d'), self.name)

	class Meta:
		ordering = ['-created_at']

class Page(models.Model):
    title = models.CharField(max_length=256, verbose_name=("Page Title"))
    category = models.ForeignKey(PageCategory, related_name="page_category", on_delete="cascade")
    abstract = models.TextField()
    slug = models.SlugField(max_length = 250, null = False, blank = False, editable=False)
    content  = RichTextUploadingField()
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs) # Call the real save() method
	

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    class Meta:
        ordering = ['-created_at']


