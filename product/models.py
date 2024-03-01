from django.contrib.auth.models import User
from django.db import models

PAINTING_CHOICES = (
    ('acrylic', 'acrylic'),
    ('oil', 'oil'),
    ('water-color', 'water-color'),
    ('gouache', 'gouache'),
    ('digital-painting', 'digital-painting'),
    ('pastel', 'pastel'),
    ('other', 'other'),
)


# a model that use for create products and show in our website.
class Product(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(default='')
    material = models.CharField(max_length=30, null=True, blank=True)
    color = models.CharField(max_length=16)
    width = models.CharField(max_length=16, null=False, blank=False)
    length = models.CharField(max_length=20, null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=1, null=False, blank=False)
    image = models.ImageField(upload_to='products', blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    favorites = models.ManyToManyField(User, related_name='favorites', blank=True)
    painting_style = models.CharField(max_length=20, choices=PAINTING_CHOICES, default='other')

    # artist = models.ForeignKey(Artist , on_delete=models.CASCADE(),related_name='artist')
    # we can add an app called artist and get some info about an artist and his/her products,then add to this field

    # category = models.ForeignKey(Category, on_delete=models.SET_NULL())
    # we also can create another model named Category(that i created and comment below). it can be usable for
    # filtering products and searching with Category

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "products"
        verbose_name_plural = "products"
        db_table = "products"


# class Category(models.Model):
#     name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = "category"
#         verbose_name_plural = "category"
#         db_table = "category"
#
