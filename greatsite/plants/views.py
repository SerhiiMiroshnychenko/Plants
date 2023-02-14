from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect


# Create your views here.
def index(request):
    # request == посилання на клас HttpRequest
    # через request нам доступна вся поточна інформація в рамках поточного запиту
    return HttpResponse('\t<h1>Вітаємо на сайті <br>"PLANTS":<br><i> все про ароїдні рослини!</i></h1>')


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


def pageNotFound(request, exception):
    # Обробка помилки 404
    return HttpResponseNotFound('<h1>Сторінка не знайдена</h1>')
