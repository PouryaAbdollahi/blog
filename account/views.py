from django.contrib.auth.mixins import LoginRequiredMixin
from account.mixins import AvailableFieldsMixin, FormValidMixin
from blog.models import Article
from django.views.generic import ListView, CreateView
# Create your views here.


class ArticleList(LoginRequiredMixin, ListView):
    template_name = 'registration/home.html'
    context_object_name = 'articles'

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Article.objects.all()
        return user.articles.all()


class CreateArticle(LoginRequiredMixin, AvailableFieldsMixin, FormValidMixin, CreateView):
    model = Article
    template_name = 'registration/create_article.html'
