from django.http import HttpResponse


def google_search(request):
    return HttpResponse('Это станица для поисковой системы Google')


def yandex_search(request):
    return HttpResponse('Это станица для поисковой системы Yandex')
