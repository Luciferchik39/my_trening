from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


class NewsDeliteView(DeleteView):
    model = Articles
    success_url = '/news'
    template_name = 'news/news-delite.html'


class newDetailView(DetailView):
    model = Articles
    template_name = 'news/DetailView.html'
    context_object_name = 'articles'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm


def news_home(requsts):
    news = Articles.objects.order_by('-data_news')[:3]
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