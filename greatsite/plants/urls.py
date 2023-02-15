from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),  # http://127.0.0.1:8080/
    # де 'home' -> ім'я, що ми дали шляху до головної сторінки
    path('about/', about, name='about'),  # http://127.0.0.1:8080/about/
    path('cats/', categories),  # http://127.0.0.1:8000/cats/
    path('cats/<slug:cat>/', category),  # http://127.0.0.1:8000/cats/anubias/
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),  # http://127.0.0.1:8000/archive/1981/
]
