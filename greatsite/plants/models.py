from django.db import models


# Create your models here.
class Plants(models.Model):
    # Поле id вже є в базовому класі Model, прописувати його не треба
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)  # blank=True -> показує, що поле може бути пустим
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')  # upload_to -> показує в який каталог і які підкаталоги
    # ми будемо завантажувати наші фото
    time_create = models.DateTimeField(auto_now_add=True)  # auto_now_add=True -> поле приймає поточний час
    # при додаванні нового запису і більше не змінюється
    time_update = models.DateTimeField(auto_now=True)  # auto_now=True -> буде автоматично змінюватися кожен раз,
    # коли ми щось змінюємо в допису
    is_published = models.BooleanField(default=True)  #
