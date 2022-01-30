"""DjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings

from django.conf.urls.static import static
from django.contrib import admin #自带的admin站点

from django.urls import path, include

#定义前端路由页面    返回定义的函数
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls), #自带的admin站点
    #默认进入http://127.0.0.1:8000/books/ 自动跳转到booktest应用下的子路由
    path('books/',include('booktest.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
    path('index/',appviews.index),
    path('detail/',appviews.detail),
    path('orm/',appviews.orm),
    path('orm/del/',appviews.ormdel),
    path('orm/select/', appviews.ormlist),
    path('orm/update/',appviews.ormupdate),
    
"""