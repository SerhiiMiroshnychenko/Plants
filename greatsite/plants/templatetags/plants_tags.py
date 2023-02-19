from django import template
from plants.models import *


register = template.Library()


# Функція декорована @register.simple_tag() => перетворюється в простий тег
@register.simple_tag(name='getcats')
def get_categories(filter=None):
    """
    Функція - простий тег
    Простий тег повертає колекцію даних,
    яку ми можемо використовувати в HTML шаблоні
    """
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


@register.inclusion_tag('plants/list_categories.html')  # Шаблон куди передається словник в return-і
def show_categories(sort=None, cat_selected=0):
    """
    Функція - тег включення
    Тег включення - формує та повертає фрагмент HTML сторінки
    """
    if not sort:
        cats = Category.objects.all()  # Читає всі категорії
    else:
        cats = Category.objects.order_by(sort)

    return {"cats": cats, "cat_selected": cat_selected}  # Повертає словник в шаблон 'plants/list_categories.html'
