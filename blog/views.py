from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Article, Category
from django.contrib.auth import get_user_model
# Create your views here.

User = get_user_model()


class ArticleList(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'articles'
    paginate_by = 2
    queryset = Article.objects.get_published_articles()


class ArticleDetail(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'


class CategoryArticleList(ListView):
    context_object_name = 'articles'
    template_name = 'blog/artilcle_by_category.html'
    paginate_by = 2

    def get_queryset(self):
        global category
        category = Category.objects.get(slug=self.kwargs['slug'])
        return category.articles.get_published_articles()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context


class AuthorArticleList(ListView):
    template_name = 'blog/article_by_author.html'
    paginate_by = 2
    context_object_name = 'articles'

    def get_queryset(self):
        global author
        username = self.kwargs['username']
        author = User.objects.get(username=username)
        return author.articles.get_published_articles()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context
