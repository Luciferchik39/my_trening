from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
# Create your views here.

def news_home(requsts):
    news = Articles.objects.order_by('-data_news')
    return render(requsts, "news/news_home.html", {'news': news})

def create(reqests):
    error = ""
    if reqests.method == 'POST':
        form = ArticlesForm(reqests.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = "Форма заполенна не верно"

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(reqests, "news/create.html", data)