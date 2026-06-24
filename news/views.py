from django.shortcuts import render, get_object_or_404
from .models import News, Category

def home(request):
    news = News.objects.all()
    lang = request.GET.get('lang', 'en')

    return render(request, 'news/home.html', {
        'news': news,
        'lang': lang
    })

def detail(request, id):
    article = get_object_or_404(News, id=id)
    lang = request.GET.get('lang', 'en')

    return render(request, 'news/detail.html', {
        'article': article,
        'lang': lang
    })