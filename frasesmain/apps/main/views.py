from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from .models import Category, Post

class HomeView(TemplateView):

	template_name = 'home.html'

	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		context['categories'] = Category.objects.filter(public=True).order_by('-created_at')
		context['posts'] = Post.objects.filter(public=True).order_by('-created_at')
		return context


class CategoryDetail(TemplateView):

	template_name = 'category_detail.html'

	def get_context_data(self, **kwargs):
		context = super(CategoryDetail, self).get_context_data(**kwargs)
		current_category = get_object_or_404(Category, slug=kwargs['slug'])
		current_category.seen += 1
		current_category.save()
		context['current_category'] = current_category
		context['categories'] = Category.objects.filter(public=True).order_by('-created_at')
		context['posts'] = Post.objects.filter(category=current_category).order_by('-created_at')
		return context

class PostDetail(TemplateView):

	template_name = 'detail.html'

	def get_context_data(self, **kwargs):
		context = super(PostDetail, self).get_context_data(**kwargs)
		category = get_object_or_404(Category, slug=kwargs['category'])
		post = get_object_or_404(Post, slug=kwargs['slug'])
		post.seen += 1
		post.save()
		context['category'] = category
		context['categories'] = Category.objects.filter(public=True).order_by('-created_at')
		context['post'] = post
		context['last_posts'] = Post.objects.filter(public=True).exclude(slug=post.slug).select_related('category').order_by('-created_at')[:6]
		context['phrases'] = post.phrases.all()
		return context

