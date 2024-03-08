from django.db import models


class BlogNews(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
