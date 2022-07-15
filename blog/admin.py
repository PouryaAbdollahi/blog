from django.contrib import admin
from django.contrib.admin import register
from blog.models import Article, Category
# Register your models here.


def make_published(model_admin, request, queryset):
    queryset.update(status='P')


def make_drafted(model_admin, request, queryset):
    queryset.update(status='D')


@register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'get_article_thumbnail', 'get_category', 'created_at', 'publish_date', 'last_update', 'status']
    search_fields = ['slug']
    list_filter = ['status']
    actions = [make_published, make_drafted]
    prepopulated_fields = {'slug': ('title',)}


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'parent', 'is_active']
    search_fields = ['title', 'slug']
    list_filter = ['is_active']
