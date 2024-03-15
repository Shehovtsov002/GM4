from django.db import models


class BlogNews(models.Model):
    TYPE_NEWS_CHOICES = (
        ('Шоу бизнес', 'Шоу бизнес'),
        ('Авто', 'Авто'),
        ('Вечерний Бишкек', 'Вечерний Бишкек'),
        ('Технологии', 'Технологии')
    )

    title = models.CharField(max_length=100, null=True, verbose_name="Напишите название новости")
    description = models.TextField(null=True, verbose_name="Напишите новость")
    publication_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', null=True, verbose_name="Загрузите фото")
    music = models.FileField(upload_to='music/', null=True, verbose_name="Загрузите аудио")
    type_news = models.CharField(null=True, max_length=100, choices=TYPE_NEWS_CHOICES,
                                 verbose_name="Выберите тип новости")
    youtube_url = models.URLField(null=True, verbose_name="Ссылка на ютуб")
    price = models.PositiveIntegerField(null=True, blank=True, default=100,
                                        verbose_name="Укажите цену")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
