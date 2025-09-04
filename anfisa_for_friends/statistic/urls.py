from django.urls import path

from . import views

app_name = 'statistic'

urlpatterns = [
    path('google/', views.google_search, name='google_search'),
    path('yandex/', views.yandex_search, name='yandex_search'),
]
