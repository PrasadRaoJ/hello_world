from django.shortcuts import render

# Create your views here.

from .models import Article

def home(request):

    articles = Article.objects.order_by('-created_at')

    context ={
        'articles': articles,
    }

    return render(request, 'index.html',context)