from django.contrib import admin

from .models import Category, Phrase, Author

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	
	list_display = ('name', )

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	
	list_display = ('name', )

@admin.register(Phrase)
class PhraseAdmin(admin.ModelAdmin):
	
	list_display = ('phrase', 'category', 'author' )
	list_editable = ('author', )
