from django.urls import path, re_path
from blog.views import ArticleList, ArticleDetail, CategoryArticleList, AuthorArticleList

app_name = 'blog'
urlpatterns = [
    path('', ArticleList.as_view(), name='home'),
    re_path(r'^article/(?P<slug>[-\w]+)/$', ArticleDetail.as_view(), name='detail'),
    re_path(r'^category/(?P<slug>[-\w]+)/$', CategoryArticleList.as_view(), name='category-article'),
    path('author/<slug:username>', AuthorArticleList.as_view(), name='author-article')
]