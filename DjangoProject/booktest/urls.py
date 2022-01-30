from django.urls import path, include
#这是django2，3，4以上版本都用path 了  只有1版本还在用url

from booktest import views as bookviews
#导入app里的views文件

#使用REST框架 路由
from rest_framework.routers import DefaultRouter

#路由路径定义列表：
urlpatterns=[
    # 当页面跳转到 http://127.0.0.1:8000/books/下则会调用的接口
    # path("",bookviews.BookInfoViewSet.as_view({'get':'list','post': 'create'})),

    #get请求携带query的形参 http://127.0.0.1:8000/books/:pk   :pk是形参
    # path("<str:pk>" ,bookviews.BookInfoViewSet.as_view({'get':'retrieve','put': 'update','delete': 'destroy'})),

    #------自定义请求路由 响应get请求使用latest方法 查询最新的一条记录------#
    # path("latest/",bookviews.BookInfoViewSet.as_view({"get":'latest','delete':"deleteLatest"})),
    #http://127.0.0.1:8000/books/:pk/price/ 响应get和put请求 实现查找单一 修改price字段
    # path("<str:pk>/price/", bookviews.BookInfoViewSet.as_view({'get':'retrieve','put':"price"}))
]
#实例化
router = DefaultRouter()
#创建路由器（路由url的地址，指定一个视图集）
router.register("books",bookviews.BookInfoViewSet)
router.register("heros",bookviews.HeroInfoViewSet)

#生成路由插入到上面定义的urlpatterns路由路径列表里面
urlpatterns += router.urls
# router.register("herolist",bookviews.HeroInfoViewSet)
# router.register('',bookviews.BookViewSet)


# path("/<str:ids>" ,bookviews.BookDetailView.get),
# path("adds",bookviews.BookListView.post),
# path("edit/<str:ids>" ,bookviews.BookDetailView.put),
# path("delete/<str:ids>" ,bookviews.BookDetailView.delete),

