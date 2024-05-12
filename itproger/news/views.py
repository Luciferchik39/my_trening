from django.shortcuts import render

# Create your views here.

def news_home(requsts):
    data = {
        'title': "что то о новостях"

    }
    return render(requsts, "news/news_home.html", data)