from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.

User = get_user_model()


class ArticleManager(models.Manager):
    def get_published_articles(self):
        return self.filter(status='P').order_by('-publish_date')


class CategoryManager(models.Manager):
    def get_active_categories(self):
        return self.filter(is_active=True)


class Article(models.Model):
    STATUS_CHOICE = (
        ('P', 'published'),
        ('D', 'drafted')
    )
    title = models.CharField(max_length=150, verbose_name='عنوان')
    slug = models.SlugField(max_length=170, unique=True, blank=True, allow_unicode=True, verbose_name='اسلاگ')
    thumbnail = models.ImageField(upload_to='images/article_thumbnail/', verbose_name='تصویر مقاله')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='نویسنده', related_name='articles')
    category = models.ManyToManyField('Category', verbose_name='دسته بندی', blank=True, related_name='articles')
    content = models.TextField(verbose_name='متن')
    created_at = models.DateTimeField(auto_now_add=timezone.now, verbose_name='تاریخ ایجاد')
    publish_date = models.DateTimeField(default=timezone.now, verbose_name='تاریخ انتشار')
    last_update = models.DateTimeField(auto_now=timezone.now, verbose_name='آخرین بروزرسانی')
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, verbose_name='وضعیت')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def get_absolute_url(self):
        return reverse('account:home')

    def get_active_categories(self):
        return self.category.filter(is_active=True)

    def get_article_thumbnail(self):
        return format_html(f"<img width=100em height=75em style='border-radius: 5px;' src={self.thumbnail.url}>")

    get_article_thumbnail.short_description = 'تصویر مقاله'

    def get_category(self):
        return ' , '.join([str(c) for c in self.get_active_categories()])

    get_category.short_description = 'دسته بندی'

    objects = ArticleManager()


class Category(models.Model):
    title = models.CharField(max_length=64, verbose_name='عنوان')
    slug = models.SlugField(max_length=128, unique=True, blank=True, allow_unicode=True, verbose_name='اسلاگ')
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL,
                               related_name='children', verbose_name='دسته بندی والد')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیر فعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    objects = CategoryManager()
