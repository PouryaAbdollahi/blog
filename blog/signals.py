from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from blog.models import Article, Category


def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title, allow_unicode=True)

    instance_class = instance.__class__
    qs = instance_class.objects.filter(slug=slug)
    if qs.exists():
        new_slug = f'{instance.title.replace(" ", "-")}-{qs.first().id}'
        return unique_slug_generator(instance, new_slug)

    return slug


@receiver(pre_save, sender=Article)
def create_article(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


@receiver(pre_save, sender=Category)
def create_category(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)
