from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:pk>/', get_category, name='category'),
    path('news/<int:pk>/', view_news, name='view_news'),
    path('news/add-news/', add_news, name='add_news'),
]