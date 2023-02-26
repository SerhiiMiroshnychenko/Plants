from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', PlantsHome.as_view(), name='home'),  # http://127.0.0.1:8080/
    # path('', index, name='home'),  # http://127.0.0.1:8080/
    # де 'home' -> ім'я, що ми дали шляху до головної сторінки
    path('about/', about, name='about'),  # http://127.0.0.1:8080/about/
    path('cats/', categories),  # http://127.0.0.1:8000/cats/
    path('cats/<slug:cat>/', category),  # http://127.0.0.1:8000/cats/anubias/
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),  # http://127.0.0.1:8000/archive/1981/
    path('addpage/', AddPage.as_view(), name='add_page'),
    # path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    # path('post/<slug:post_slug>/', show_post, name='post'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    # path('category/<int:cat_id>', show_category, name='category'),
    path('category/<slug:cat_slug>/', PlantsCategory.as_view(), name='category'),
]
