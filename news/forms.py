from django import forms
from django.db import models
from django.forms import fields, widgets

from .models import News #Category


class NewsForm(forms.ModelForm): #(forms.Form):
    # title = forms.CharField(max_length=150, label='Название', widget=forms.TextInput(attrs={'class': 'form-control',}))
    # content = forms.CharField(label='Текст новости', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 8}))
    # is_published = forms.BooleanField(label='Опубликовано', initial=True, required=False)
    # category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Выбрать категорию', widget=forms.Select(attrs={'class': 'form-control',}))
    
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title','category', 'content', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',}),
            'category': forms.Select(attrs={'class': 'form-control',}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 8}),
        }
