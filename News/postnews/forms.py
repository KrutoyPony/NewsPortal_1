from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'id_author',
            'id_post_category',
            'article_title_news',
            'main_text'
        ]