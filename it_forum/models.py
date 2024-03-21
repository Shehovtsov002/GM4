from django.db import models


class ItForum(models.Model):
    name = models.CharField(max_length=100, verbose_name='Input your name')
    email = models.EmailField(verbose_name='Input your email', blank=True, null=True)
    description = models.TextField(verbose_name='Describe your trouble', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Вопросы про пайтон'
        verbose_name = 'Вопрос'
