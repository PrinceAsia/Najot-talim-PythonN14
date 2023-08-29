from django.shortcuts import render


# Create your views here.
def MainPageView(request):
    return render(request, 'base.html', {})


def NewsPageView(request):
    news = ['Yangilik ' + str(i+1) for i in range(10)]
    return render(request, 'news.html', {'news': news})