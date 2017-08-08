from django.contrib import admin

from .models import Category, Phrase, Author, Post

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	
	list_display = ('name', 'slug', 'public', 'seen',)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	
	list_display = ('name', )

@admin.register(Phrase)
class PhraseAdmin(admin.ModelAdmin):
	
	list_display = ('phrase', 'category', 'author' )
	list_editable = ('author', )

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	
	def formfield_for_manytomany(self, db_field, request, **kwargs):
		if db_field.name == "phrases":
			kwargs["queryset"] = Phrase.objects.filter(post=None)
		return super(PostAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

	list_display = ('title', 'seen', 'public')
	filter_horizontal = ('phrases',)

