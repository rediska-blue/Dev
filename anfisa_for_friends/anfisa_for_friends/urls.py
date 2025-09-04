from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('homepage.urls', namespace='homepage')),
    path('about/', include('about.urls', namespace='about')),
    path('ice_cream/', include('ice_cream.urls', namespace='ice_cream')),
    path('statistic/', include('statistic.urls', namespace='statistic')),
    path('auth/', include('users.urls', namespace='users')),
    path('admin/', admin.site.urls),
]
