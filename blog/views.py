from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.utils import timezone
from datetime import datetime

from .models import ArticleModel
from .forms import ArticleForm


class Home(View):
    def get(self, request):
        return HttpResponse('hello')

    def post(self, request):
        return HttpResponse('bye')


class Article(View):
    def get(self, request):
        articles = ArticleModel.objects.all()

        return render(request, "articles.html", {"articles": articles, "form": ArticleForm()})

    def post(self, request):
        form = ArticleForm(request.POST)
        form.instance.created_at = datetime.now(tz=timezone.utc)
        form.save()

        return redirect('/blog/articles')

        # title = request.POST['title']
        # category = request.POST['category']
        # author = request.POST['author']
        # content = request.POST['content']

        # ArticleModel.objects.create(
        #     title=title,
        #     category=category,
        #     author=author,
        #     content=content,
        #     created_at=datetime.now(tz=timezone.utc)
        # )

        # return redirect('/blog/articles')
