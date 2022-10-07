from django.shortcuts import render
from articles.models import Article, Relationship, Tag


def articles_list(request):
    template = 'articles/news.html'
    context = {
        'object_list': Article.objects.all()
    }
    ordering = '-published_at'

    return render(request, template, context)

def students_list(request):
    template = 'school/students_list.html'
    context = {
        'object_list': (Student.objects.all().order_by('group')
                        .prefetch_related('teachers'))
    }

    return render(request, template, context)