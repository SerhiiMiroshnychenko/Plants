from django.contrib import admin
from .models import *


# Register your models here.
class PlantsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')  # Перелік полів,
    # які ми хочемо бачити в адмін-панелі
    list_display_links = ('id', 'title')  # Поля за якими можна перейти на відповідну статтю
    search_fields = ('title', 'content')  # За якими полями можна буде проводити пошук
    list_editable = ('is_published',)  # Робимо поле is_published таким, що можна редагувати з адмін-панелі
    list_filter = ('is_published', 'time_create')  # Призначаємо поля для фільтрації списку статей


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Plants, PlantsAdmin)
admin.site.register(Category, CategoryAdmin)
