from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    # request == посилання на клас HttpRequest
    # через request нам доступна вся поточна інформація в рамках поточного запиту
    return HttpResponse('Сторінка додатку "Plants"')
