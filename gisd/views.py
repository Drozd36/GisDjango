from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from gisd.models import Articles


def home(request):
    #  return HttpResponse("Hello world")
    # return render(request, 'giss/home.html')
    articles = Articles.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'giss/home.html', context)


def about(request):
    return render(request, 'giss/about.html')


def show_articles(request, article_id):
    article = get_object_or_404(Articles, id=article_id)
    return render(request, 'giss/article.html', {'article': article})