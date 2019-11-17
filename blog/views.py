from django.shortcuts import render
from django.http import HttpResponse
from . import models


# 文章首页
def index(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


# 文章详情
def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})


# 添加页面
def add_page(request):
    return render(request, 'blog/add_page.html')


# 提交添加
def add_action(request):
    title = request.POST['title']
    content = request.POST['content']
    models.Article.objects.create(title=title, content=content)
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


# 编辑页面
def edit_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', {'article': article})


# 提交编辑
def edit_action(request):
    # articles = models.Article.objects.all()
    # return render(request, 'blog/index.html', {'articles': articles})
    id = request.POST['id']
    title = request.POST['title']
    content = request.POST['content']
    if id == '0':
        models.Article.objects.create(title=title, content=content)
        articles = models.Article.objects.all()
        return render(request, 'blog/index.html', {'articles': articles})
    article = models.Article.objects.get(pk=id)
    article.title = title
    article.content = content
    article.save()
    return render(request, 'blog/article_page.html', {'article': article})
