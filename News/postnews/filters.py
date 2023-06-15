from django_filters import FilterSet
from .models import Post, Author

class PostFilter(FilterSet):
	class Meta:

		model = Post

		fields = {
			'article_title_news': ['icontains'],
			'id_author': ['exact'],
			'time_create': ['date__gt']

		}
