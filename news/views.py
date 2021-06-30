from django import forms
from django.shortcuts import render, get_object_or_404, redirect

from .models import News, Category
from .forms import NewsForm


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
    return render(request, 'news/category.html', context)


def view_news(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    context = {'news_item': news_item}
    return render(request, 'news/view_news.html', context)


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = News.objects.create(**form.cleaned_data)
            return redirect(news)
    else:
        form = NewsForm()
    context = {'form': form}
    return render(request, 'news/add_news.html', context)
