from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)


class meta:
    def __init__(self):
        pass

    ordering = 'name'
    verbose_name = 'category'
    verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('shope:products_by_category', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class Product(models.Model):
    objects = None
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def get_url(self):
        return reverse('shope:prodCatdetail',args=[self.category.slug,self.slug])

    class meta:
        ordering = 'name'
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return '{}'.format(self.name)
