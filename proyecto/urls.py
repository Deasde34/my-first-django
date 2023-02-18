"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from libreria import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('admin/', admin.site.urls),
    path('about/', views.about, name = 'about'),
    path('contact',views.contact, name = 'contact'),
    path('pageFour',views.pageFour, name = 'pageFour'),
    path('pageFive',views.pageFive, name = 'pageFive'),
    path('pageSix',views.pageSix, name = 'pageSix'),
    path('pageSeven',views.pageFour, name = 'pageSeven'),
    path('pageEight',views.pageFive, name = 'pageEight'),
    path('pageNine',views.pageSix, name = 'pageNine'),
    path('pageTen',views.pageSix, name = 'pageTen'),
    path('pageEleven',views.pageSix, name = 'pageEleven'),
    path('pageTwelve',views.pageSix, name = 'pageTwelve'),
    path('pageThirteen',views.pageSix, name = 'pageThirteen'),

]
