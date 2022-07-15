from django import template
from blog.models import Category

register = template.Library()


@register.inclusion_tag('../templates/blog/partials/navbar_category.html')
def show_category():
    all_categories = Category.objects.get_active_categories()
    return {'categories': all_categories}
