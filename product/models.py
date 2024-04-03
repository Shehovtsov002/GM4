from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='Inter tag', default='#')

    def __str__(self):
        return f'#{self.name}'


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Inter title')
    description = models.TextField(verbose_name='Inter description', blank=True)
    price = models.PositiveIntegerField(verbose_name='Inter price', default=0)
    tags = models.ManyToManyField(Tag, verbose_name='Tags')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    def __str__(self):
        return f'{self.title}'
