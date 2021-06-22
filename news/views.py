from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import News, Category


def index(request):
    news = News.objects.all()
    context = {
        'news': news, 
        'title': 'Список новостей',
        }
    return render(request, 'news/index.html', context)


def get_category(request, pk):
    news = News.objects.filter(category_id=pk)
    category = Category.objects.get(pk = pk)
    context = {'news':news, 'category':category}
    return render(request, template_name='news/category.html', context=context)