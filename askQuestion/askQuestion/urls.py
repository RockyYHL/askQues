"""askQuestion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path
from wjdc import views,toBase

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^test/$', views.test, name='test'),
    #parents
    url(r'^index/B_RT/B_RT-info/$', views.parents, name='B_RT-info'),
    url(r'^index/B_RT/B_RT-1/$', views.parents2, name='B_RT-1'),
    url(r'^index/B_RT/B_RT-2/$', views.parents3, name='B_RT-2'),
    url(r'^index/B_RT/B_RT-3/$', views.parents4, name='B_RT-3'),
    #students
    url(r'^index/B_XS/B_XS-info/$', views.students, name='B_XS-info'),
    url(r'^index/B_XS/B_XS-1/$', views.students2, name='B_XS-1'),
    url(r'^index/B_XS/B_XS-2/$', views.students3, name='B_XS-2'),
    url(r'^index/B_XS/B_XS-3/$', views.students4, name='B_XS-3'),
    #adult
    url(r'^index/B_CR/B_CR-info/$', views.adult, name='B_CR-info'),
    url(r'^index/B_CR/B_CR-1/$', views.adult2, name='B_CR-1'),
    url(r'^index/B_CR/B_CR-2/$', views.adult3, name='B_CR-2'),
    url(r'^index/B_CR/B_CR-3/$', views.adult4, name='B_CR-3'),
    #endpage
    url(r'^index/endpage/$', views.endpage, name='endpage'),
    #jiekou
    url(r'^api/setToBase1/$', toBase.setToBase1, name='toBase1'),
    url(r'^api/setToBase2/$', toBase.setToBase2, name='toBase2'),
    url(r'^api/setToBase3/$', toBase.setToBase3, name='toBase3'),
]
