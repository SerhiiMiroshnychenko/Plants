from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *


menu = [{'title': "Про сайт", 'url_name': 'about'},
        {'title': "Додати статтю", 'url_name': 'add_page'},
        {'title': "Зворотній зв'язок", 'url_name': 'contact'},
        {'title': "Вхід", 'url_name': 'login'}]


# Create your views here.
class PlantsHome(DataMixin, ListView):
    model = Plants  # Модель список екземплярів якої будемо подавати
    template_name = 'plants/index.html'  # Адреса шаблону, куди подавати
    context_object_name = 'posts'  # Ім'я з яким викликається в шаблоні index.html

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # Передаємо вже сформований контекст
        # context['menu'] = menu
        # context['title'] = 'Головна сторінка'
        # context['cat_selected'] = 0
        # return context
        c_def = self.get_user_context(title="Головна сторінка")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Plants.objects.filter(is_published=True)


# def index(request):
#     # request == посилання на клас HttpRequest
#     # через request нам доступна вся поточна інформація в рамках поточного запиту
#     # return HttpResponse('<h1>Вітаємо на сайті <br>"PLANTS":<br><i> все про ароїдні рослини!</i></h1>')
#     posts = Plants.objects.all()  # Посилання на всі записи бази даних
#
#     context_dict = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Додаток PLANTS',
#         'cat_selected': 0,
#                }
#     return render(request, 'plants/index.html',
#                   context=context_dict)


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


class AddPage(DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'plants/addpage.html'
    success_url = reverse_lazy('home')  # Маршрут, куди ми перейдемо після додавання статті
    # Функція reverse_lazy - будує маршрут коли він буде потрібен, а не наперед
    # Це запобігає помилці, коли маршрут намагається побудуватися, коли django
    # Ще його не побудував

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = 'Додавання статті'
        # context['menu'] = menu
        # return context
        c_def = self.get_user_context(title="Додавання статті")
        return dict(list(context.items()) + list(c_def.items()))

# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             #print(form.cleaned_data)
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     return render(request, 'plants/addpage.html', {'form': form, 'menu': menu, 'title': 'Додавання статті'})



def contact(request):
    return HttpResponse("Зворотній зв'язок")


def login(request):
    return HttpResponse('Вхід')


class ShowPost(DataMixin, DetailView):
    model = Plants
    template_name = 'plants/post.html'  # Шаблон за яким буде подаватися
    slug_url_kwarg = 'post_slug'  # Слаг для подання в URL
    # pk_url_kwarg = 'post_pk'
    context_object_name = 'post'  # Ім'я під яким викликається в шаблоні post.html

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = context['post']
        # context['menu'] = menu
        # return context
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))

# def show_post(request, post_slug):
#     # post = get_object_or_404(Plants, slug=post_slug)
#     post = get_object_or_404(Plants, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#
#     return render(request, 'plants/post.html', context=context)


class PlantsCategory(DataMixin, ListView):
    model = Plants
    template_name = 'plants/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Plants.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = 'Категорія - ' + str(context['posts'][0].cat)
        # context['menu'] = menu
        # context['cat_selected'] = context['posts'][0].cat_id
        # return context
        c_def = self.get_user_context(title='Категорія - ' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))

# def show_category(request, cat_id):
#     posts = Plants.objects.filter(cat_id=cat_id)
#
#     # if len(posts) == 0:
#         # raise Http404()
#
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Відображення за рубриками',
#         'cat_selected': cat_id,
#     }
#
#     return render(request, 'plants/index.html', context=context)


def pageNotFound(request, exception):
    # Обробка помилки 404
    return HttpResponseNotFound('<h1>Сторінка не знайдена</h1>')
