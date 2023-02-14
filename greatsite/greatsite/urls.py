"""greatsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from greatsite import settings
from plants.views import *


urlpatterns = [
    path('admin/', admin.site.urls),  # Звернення до "адмінки" нашого сайту
    path('', include('plants.urls')),  # Передаємо посилання urls на додатку plants
    # І вони починаються з головної сторінки

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound  # Сторінка не знайдена

# handler500 -> помилка серверу
# handler403 -> доступ заборонено
# handler400 -> неможливо обробити запит
