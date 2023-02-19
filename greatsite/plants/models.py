from django.db import models
from django.urls import reverse


# Create your models here.
class Plants(models.Model):
    # Поле id вже є в базовому класі Model, прописувати його не треба
    title = models.CharField(max_length=255, verbose_name='Вид рослини')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name='Текст статті')  # blank=True -> показує, що поле може бути пустим
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')  # upload_to -> показує в який каталог і які підкаталоги
    # ми будемо завантажувати наші фото
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Час створення')  # auto_now_add=True -> поле приймає поточний час
    # при додаванні нового запису і більше не змінюється
    time_update = models.DateTimeField(auto_now=True, verbose_name='Час змінення')  # auto_now=True -> буде автоматично змінюватися кожен раз,
    # коли ми щось змінюємо в допису
    is_published = models.BooleanField(default=True, verbose_name='Публікація')  #
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категорія')  # 'Category' - у вигляді стрічки позаяк визначення
    # класу Category відбувається після моделі Plants

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Ароїдні рослини'
        verbose_name_plural = 'Ароїдні рослини'
        # ordering = ['-time_create', 'title']
        ordering = ['title']  # Задаємо сортування в адмін-панелі
        # та на сайті (в списку екземплярів моделі Plants)


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категорія')  # db_index=True => поле буде індексовано,
    # пошук по ньому буде відбуватися швидше
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['id']
