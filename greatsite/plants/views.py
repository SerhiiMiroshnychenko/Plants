from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render
from .models import *


menu = [{'title': "Про сайт", 'url_name': 'about'},
        {'title': "Додати статтю", 'url_name': 'add_page'},
        {'title': "Зворотній зв'язок", 'url_name': 'contact'},
        {'title': "Вхід", 'url_name': 'login'}]


# Create your views here.
def index(request):
    # request == посилання на клас HttpRequest
    # через request нам доступна вся поточна інформація в рамках поточного запиту
    # return HttpResponse('<h1>Вітаємо на сайті <br>"PLANTS":<br><i> все про ароїдні рослини!</i></h1>')
    posts = Plants.objects.all()  # Посилання на всі записи бази даних

    context_dict = {
        'posts': posts,
        'menu': menu,
        'title': 'Додаток PLANTS',
        'cat_selected': 0,
               }
    return render(request, 'plants/index.html',
                  context=context_dict)


def about(request):
    return render(request, 'plants/about.html', {'title': 'Про сайт', 'menu': menu})



def categories(request):

    return HttpResponse('<h1>Дописи по категоріям</h1><p>Оберіть категорію</p>')


def category(request, cat):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Дописи по категоріям</h1><h2>- Категорія: "<i>{cat}</i>"</h2>')


def archive(request, year):
    if int(year) > 2023:  # Якщо рік > 2023 => генеруємо виключення 404
        raise Http404()
    elif int(year) == 2023:  # Якщо рік == 2023 => перехід на головну сторінку
        # return redirect('/') -> тимчасовий redirect
        # return redirect('/', permanent=False) -> постійний redirect
        return redirect('home', permanent=False)  # Де "home" - ім'я URL адреси головної сторінки

    return HttpResponse(f'<h1>Архів за минулі роки</h1><hr><p>{year} рік</p>')


def addpage(request):
    return HttpResponse('Додати статтю')


def contact(request):
    return HttpResponse("Зворотній зв'язок")


def login(request):
    return HttpResponse('Вхід')


def show_post(request, post_id):
    return HttpResponse(f'Відображення статті з id = {post_id}')


def show_category(request, cat_id):
    posts = Plants.objects.filter(cat_id=cat_id)

    # if len(posts) == 0:
        # raise Http404()


    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Відображення за рубриками',
        'cat_selected': cat_id,
    }

    return render(request, 'plants/index.html', context=context)



def pageNotFound(request, exception):
    # Обробка помилки 404
    return HttpResponseNotFound('<h1>Сторінка не знайдена</h1>')
