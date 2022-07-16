from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from account.mixins import AvailableFieldsMixin, FormValidMixin, AuthorAccessMixin, SuperUserAccessMixin
from blog.models import Article
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Create your views here.


class ArticleList(LoginRequiredMixin, ListView):
    template_name = 'registration/home.html'
    context_object_name = 'articles'

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Article.objects.all()
        return user.articles.all()


class CreateArticle(LoginRequiredMixin, AvailableFieldsMixin, FormValidMixin, SuccessMessageMixin, CreateView):
    model = Article
    template_name = 'registration/create_and_update_article.html'
    # success_message = 'مقاله با موفقیت ایجاد شد.'


class ArticleUpdate(AuthorAccessMixin, AvailableFieldsMixin, FormValidMixin, SuccessMessageMixin, UpdateView):
    model = Article
    template_name = 'registration/create_and_update_article.html'
    # success_message = 'مقاله مورد نظر با موفقیت ویرایش شد.'


class ArticleDelete(SuperUserAccessMixin, SuccessMessageMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('account:home')
    template_name = 'registration/article_confirm_delete.html'
    # success_message = 'مقاله مورد نظر با موفقیت حذف شد.'

