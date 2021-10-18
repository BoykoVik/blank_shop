from django.db import models
from django.db.models.expressions import OrderBy
from django.db.models.fields import TextField

class Category(models.Model):#категории товара
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)#для URL-ов

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name

class Product(models.Model):#товары
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)#для URL-ов
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)#описание товара
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)#наличие товара
    created = models.DateTimeField(auto_now_add=True)#время создания товара
    updated = models.DateTimeField(auto_now_add=True)#время последнего изменения товара

    class Meta:
        ordering = ['name']
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name