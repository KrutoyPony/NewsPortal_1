from django.shortcuts import render
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView,

	)
from .models import Author, Post, Category
from .filters import PostFilter
from .forms import PostForm
from datetime import datetime
from django.urls import reverse_lazy

# Create your views here.


class PostMany(ListView):

	model = Post
	ordering = '-time_create'
	template_name = 'post_one.html'
	context_object_name = 'post'
	# Вывод не более 10 новостей
	paginate_by = 10

	def get_queryset(self):

		queryset = super().get_queryset()
		self.filterset = PostFilter(self.request.GET, queryset)

		return self.filterset.qs

	def get_context_data(self, **kwargs):

		context = super().get_context_data(**kwargs)
		context['filterset'] = self.filterset

		return context

class CategoryMany(ListView):
	model = Category
	ordering = 'name'
	template_name = 'category_many.html'
	context_object_name = 'categoryes'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['time_now'] = datetime.utcnow()
		context['next_sale'] = None
		return context

# Представление поиска постов
class PostSearch(ListView):

	model = Post
	template_name = 'news_search.html'
	context_object_name = 'post_search'

	def get_queryset(self):

		queryset = super().get_queryset()
		self.filterset = PostFilter(self.request.GET, queryset)

		return self.filterset.qs

	def get_context_data(self, **kwargs):

		context = super().get_context_data(**kwargs)
		context['filterset'] = self.filterset

		return context

# Представления 'Новости'
class NewsCreate(CreateView):
	form_class = PostForm
	model = Post
	template_name = 'news_create.html'

	def form_valid(self, form):
		news = form.save(commit=False)
		news.post_or_new = 'Новость'
		return super().form_valid(form)

class NewsDetail(DetailView):

	model = Post
	template_name = 'news_detail.html'
	context_object_name = 'news'

class NewsEdit(UpdateView):

	form_class = PostForm
	model = Post
	template_name = 'news_edit.html'

class NewsDel(DeleteView):

	model = Post
	template_name = 'news_delete.html'
	success_url = reverse_lazy('post_list')



# Представления 'Статьи'
class ArticlesCreate(CreateView):

	form_class = PostForm
	model = Post
	template_name = 'articles_create.html'

	def form_valid(self, form):
		articles = form.save(commit=False)
		articles.post_or_new = 'Статья'
		return super().form_valid(form)

class ArticlesDetail(DetailView):

	model = Post
	template_name = 'articles_detail.html'
	context_object_name = 'articles'

class ArticlesEdit(UpdateView):

	form_class = PostForm
	model = Post
	template_name = 'articles_edit.html'

class ArticlesDel(DeleteView):

	model = Post
	template_name = 'articles_delete.html'
	success_url = reverse_lazy('post_list')


