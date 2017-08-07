from django.db import models
from django.template.defaultfilters import slugify
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):

	name = models.CharField(max_length=50)
	slug = models.SlugField(unique=True, max_length=50)
	public = models.BooleanField(default=False)
	description = models.TextField(max_length=1000)
	seen = models.IntegerField(default=0)

	title_page = models.CharField(max_length=100)
	meta_description = models.TextField(max_length=155)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class Author(models.Model):

	name = models.CharField(max_length=100)
	slug = models.SlugField(unique=True, editable=False, max_length=70)

	description = models.TextField(max_length=1000)

	def __str__(self):
		return self.name

	def save(self):
		self.slug = slugify(self.name)
		super(Author, self).save()


class Phrase(models.Model):

	category = models.ForeignKey(Category)
	author = models.ForeignKey(Author, null=True, blank=True)
	phrase = models.TextField(max_length=1000)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.phrase


class Post(models.Model):

	category = models.ForeignKey(Category)
	title = models.CharField(max_length=70)
	image = models.ImageField(upload_to='posts')
	slug = models.SlugField(unique=True, max_length=70)
	summary = RichTextUploadingField()

	phrases = models.ManyToManyField(Phrase, null=True, blank=True)

	content = RichTextUploadingField()

	meta_description = models.TextField(max_length=155)

	opengraph = models.ImageField(upload_to='opengraph', null=True, blank=True)
	twitter_card = models.ImageField(upload_to='twitter_card', null=True, blank=True)

	seen = models.BigIntegerField(default=0, null=True, blank=True)
	public = models.BooleanField(default=False)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	# def get_absolute_url(self):
	# 	return '/%s/%s/' % (self.category.slug, self.slug)

