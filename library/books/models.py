from django.db import models
from django.db.models.fields import related


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, help_text='Код из 13 символов <a href="https://www.isbn-international.org/content/what-isbn">(ISBN)</a>')
    price = models.DecimalField(max_length=100, decimal_places=1, max_digits=100)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.name

class OrderedBooks(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField('Book', related_name='boook')
    allprice = models.DecimalField(max_length=100, decimal_places=1, max_digits=100)

    class Meta:
        verbose_name_plural = 'Список книг'

    def __str__(self):
        return self.name
