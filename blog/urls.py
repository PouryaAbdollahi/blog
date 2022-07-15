from django.urls import path
from blog.views import ArticleList, ArticleDetail, CategoryArticleList, AuthorArticleList

app_name = 'blog'
urlpatterns = [
    path('', ArticleList.as_view(), name='home'),
    path('article/<slug:slug>/', ArticleDetail.as_view(), name='detail'),
    path('category/<slug:slug>', CategoryArticleList.as_view(), name='category-article'),
    path('author/<slug:username>', AuthorArticleList.as_view(), name='author-article')
]