"""data URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from app import views
from django.conf.urls import url
urlpatterns = [
    path('',views.home),
    path('home/',views.home),
    path('login/',views.login),
    path('dashboard/datahome/',views.datahome),
    path('dashboard/datahome/<path:objs>/',views.datasub),
    path('dashboard/',views.dashboard),
    path('dashboard/editor/',views.editor),
    path('dashboard/editor/<path:objs>/',views.editorsub),
    path('dashboard/edit/action/<str:pth>/',views.actchoose),
    path('dashboard/edit/add/dt/<str:pth>/',views.choosedt),
    #path('dashboard/edit/add/<str:pth>/<str:dt>',views.addelement),
    #path('dashboard/edit/del/<str:pth>/',views.delelement),
    #path('dashboard/edit/editel/<str:pth>/',views.editelement),
]
