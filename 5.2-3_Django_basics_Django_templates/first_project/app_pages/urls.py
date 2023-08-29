from django.urls import path

from .views import MainPageView, NewsPageView


urlpatterns = [
    path('news', NewsPageView, name='news'),
    path('', MainPageView, name='main'),
]