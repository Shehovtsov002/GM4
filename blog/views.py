from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

from blog.models import BlogNews


def post_news_view(request):
    if request.method == "GET":
        query = BlogNews.objects.all()
        return render(request, template_name='news.html',
                      context={'query': query})


def hello_world(request):
    if request.method == "GET":
        return HttpResponse(f"<h1> Hello, it's my first request in django! {datetime.now()} </h1>")
