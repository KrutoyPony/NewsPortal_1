from django.urls import path
# Импортируем созданное нами представление
from .views import (
   PostMany, 
   CategoryMany,  

   NewsCreate,
   NewsDetail,
   NewsEdit,
   NewsDel,

   ArticlesCreate,
   ArticlesDetail,
   ArticlesEdit,
   ArticlesDel,

   PostSearch,

)


urlpatterns = [
   
   # Основные пути (все посты, категории, поиск)
   path('', PostMany.as_view(), name= 'post_list'),
   path('category/', CategoryMany.as_view()),
   path('search/', PostSearch.as_view(), name= 'post_search'),

   # Пути 'Новости' (создание новостей, детальная информация по ПК новости)
   path('news/create/', NewsCreate.as_view(), name= 'news_create'),
   path('news/<int:pk>/', NewsDetail.as_view(), name= 'news_detail'),
   path('news/<int:pk>/edit/', NewsEdit.as_view(), name= 'news_edit'),
   path('news/<int:pk>/delete/', NewsDel.as_view(), name= 'news_delete'),

   # Пути 'Статьи' (создание статей, детальная информация по ПК статьи)
   path('articles/create/', ArticlesCreate.as_view(), name= 'articles_create'),
   path('articles/<int:pk>/', ArticlesDetail.as_view(), name= 'articles_detail'),
   path('articles/<int:pk>/edit/', ArticlesEdit.as_view(), name= 'articles_edit'),
   path('articles/<int:pk>/delete/', ArticlesDel.as_view(), name= 'articles_delete'),

]
