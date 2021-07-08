from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
# from django.urls import reverse_lazy

from .models import News, Category
from .forms import NewsForm


class HomeNews(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    # extra_context ={'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class NewsByCategory(ListView):
    model=News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['pk'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['pk']).name
        return context


class ViewNews(DetailView):
    model = News
    # pk_url_kwarg = 'pk'
    # template_name = 'news/news_detail.html'
    context_object_name = 'news_item'


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    # success_url = reverse_lazy('home')


# def index(request):
#     news = News.objects.all()
#     context = {
#         'news': news, 
#         'title': 'Список новостей',
#         }
#     return render(request, 'news/index.html', context)


# def get_category(request, pk):
#     news = News.objects.filter(category_id=pk)
#     category = Category.objects.get(pk = pk)
#     context = {'news':news, 'category':category}
#     return render(request, 'news/category.html', context)


# def view_news(request, pk):
#     news_item = get_object_or_404(News, pk=pk)
#     context = {'news_item': news_item}
#     return render(request, 'news/view_news.html', context)


# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             print(form.is_valid())
#             # news = News.objects.create(**form.cleaned_data)
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#     context = {'form': form}
#     return render(request, 'news/add_news.html', context)
