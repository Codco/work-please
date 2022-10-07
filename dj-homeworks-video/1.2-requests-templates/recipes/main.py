from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.now().strftime('%H:%M:%S %d.%m.%Y')
    msg = f'Текущее время и дата: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    work_dir = os.listdir(path='.')
    html = "<html><body>Список файлов в рабочей дериктории: %s.</body></html>" % work_dir
    return HttpResponse(html)
    raise NotImplemented
