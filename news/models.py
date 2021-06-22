from django.db import models
from django.urls import reverse


class News(models.Model):

    title = models.CharField(verbose_name='Название', max_length=150)
    category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.PROTECT, null=True, blank=True)
    photo = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'pk': self.pk})

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Category(models.Model):
    name = models.CharField(verbose_name='Название', max_length=50, db_index=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'pk': self.pk})

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'        
        ordering = ['name']
