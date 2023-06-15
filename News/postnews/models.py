from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

news = 'Новость'
post = 'Статья'

POSSTING = [
	(news, 'Новости'),
	(post, 'Статьи')
]
# Модель автор
class Author(models.Model):
	id_user = models.OneToOneField(User, on_delete= models.CASCADE)
	name = models.CharField(max_length= 20, default= 'NoName')
	rating = models.IntegerField(validators=[MinValueValidator(0)], default= 0)

	def update_rating(self):
		pass

	# Вывод имени автора пользователю
	def __str__(self):
		return self.name

# Модель категория
class Category(models.Model):
	name = models.CharField(max_length= 20, unique= True)

	def __str__(self):
		return self.name

# Модель пост
class Post(models.Model):
	id_author = models.ForeignKey(Author, on_delete= models.CASCADE)
	post_or_new = models.CharField(max_length=20, 
								   choices= POSSTING)
	time_create = models.DateTimeField(auto_now_add= True)
	id_post_category = models.ManyToManyField(Category, through= 'PostCategory')
	article_title_news = models.CharField(max_length= 50)
	main_text = models.TextField()
	rating = models.IntegerField(validators=[MinValueValidator(0)], default= 0)

	def dislike(self):
		if self.rating == 0:
			return f'Рейтинг минимальный: {self.rating}'
		else:
			self.rating -= 1
			self.save()

	def like(self):
		self.rating += 1
		self.save()

	def preview(self):
		return self.main_text[:124] + '...'

	def __str__(self):
		return self.article_title_news[:10]
	
	def get_absolute_url(self):
		return reverse('news_detail', args= [str(self.id)])
		

# Модель пост-категория
class PostCategory(models.Model):
	id_post = models.ForeignKey(Post, on_delete= models.CASCADE)
	id_category = models.ForeignKey(Category, on_delete= models.CASCADE)

# Модель комментарии
class Comment(models.Model):
	id_post = models.ForeignKey(Post, on_delete= models.CASCADE)
	id_user = models.ForeignKey(User, on_delete= models.CASCADE)
	text_comment = models.TextField()
	date_create = models.DateTimeField(auto_now_add= True)
	rating_comment = models.IntegerField(validators=[MinValueValidator(0)], default= 0)

	def dislike(self):
		if self.rating_comment == 0:
			return f'Рейтинг минимальный: {self.rating_comment}'
		else:
			self.rating_comment -= 1
			self.save()

	def like(self):
		self.rating_comment += 1
		self.save()
