from django.urls import path
from .views import (
    HelloWorldView,
    WeekdaysView,
    MonthsView
)

urlpatterns = [
    path('week/<str:lang>', WeekdaysView, name='week'),
    path('month/<int:num>', MonthsView, name='month'),
    path('', HelloWorldView, name='hello'),
]