from django.shortcuts import render

# Create your views here.

def index(request):
    data = {
        'title': "Главная страница",
        # создал список для тренировки вывода информации из этого файла на экран чеоез передачу данныйх в файле idex.html
        # 'values': ['some', 'helo', 'kira']
    }
    return render(request, "main/index.html", data)

def about(requsts):
    data = {
        'title': "О себе любимом"

    }
    return render(requsts, "main/about.html", data)
