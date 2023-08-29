from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def HelloWorldView(request):
    return HttpResponse('Hello world')

def WeekdaysView(request, lang):
    context_uz = {'week': 'Hafta kunlari', 'data': ['Yak', 'Du', 'Se']}
    context_en = {'week': 'Week days', 'data': ['Sun', 'Mon', 'Tu']}
    context_ru = {'week': 'Rus tilida', 'data': ['Пон', 'Вто', 'Чет']}

    if lang == 'en':
        context = context_en
    elif lang == 'ru':
        context = context_ru
    else:
        context = context_uz

    return render(request, 'home.html', context)


def MonthsView(request, num):
    context = {
        'num': num,
        'months': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June']
    }
    return render(request, 'months.html', context)