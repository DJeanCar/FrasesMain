from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):

	name = models.CharField(max_length=50)
	slug = models.SlugField(unique=True, editable=False, max_length=50)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

	def save(self):
		self.slug = slugify(self.name)
		super(Category, self).save()


class Phrase(models.Model):

	category = models.ForeignKey(Category)
	phrase = models.TextField(max_length=1000)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.phrase