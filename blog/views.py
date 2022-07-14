from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Article
# Create your views here.


def home(request):
    return render(request, 'blog/index.html')


class ArticleList(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'articles'
    paginate_by = 2
    queryset = Article.objects.get_published_articles()


class ArticleDetail(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'
