import logging
import re

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, permissions
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from booktest.models import BookInfo, HeroInfo
# 定义类 通用视图集
from booktest.serializer import BookInfoModelSerializer, HeroInfoModelSerializer, GetHeroInfoModelSerializer


# 自定义分页控制类名  要写到最前面 要不后面使用分页的类视图访问不到
class LargeResultsSetPage(PageNumberPagination):
    #http://127.0.0.1:8000/books/heros/?page=1&page_size=3 第一页显示3条
    page_query_param = 'page'  # 前端发送的当前页数关键字名
    page_size_query_param = 'page_size'  #前端发送的每页显示条数关键字名
    max_page_size = 10  #限制前端传来最大显示条数/页 超过无效


class BookInfoViewSet(ModelViewSet):
    """定义类视图"""
    #指定查询集 把数据表所有数据给这个对象
    queryset = BookInfo.objects.all()
    #
    serializer_class = BookInfoModelSerializer

    """下面可以自定义高级查询等操作的接口"""
    # detail为False, books/latest/
    @action(methods=['get'],detail=False)
    #查询最新的一本书
    def latest(self,request):
        #返回最新的图书信息
        book = BookInfo.objects.latest('id') #获取数据库最后一条数据
        serializer = self.get_serializer(book)
        return Response(serializer.data)
    #删除最新的一本书 books/deleteLatest/
    def deleteLatest(self,request):
        book = BookInfo.objects.latest('id')  # 获取数据库最后一条数据
        book.delete()
        return Response({"message":"删除成功"},status=status.HTTP_204_NO_CONTENT)

    #detail=True单一操作,传一个pk books/:pk/price
    @action(methods=['put'],detail=True)
    #修改图书的价格
    def price(self,request,pk):
        book = self.get_object()#拿到要修改的id
        book.price = request.data.get('price')
        serializer = self.get_serializer(book)
        book.save()
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

class HeroInfoViewSet(ModelViewSet):
    queryset = HeroInfo.objects.all()
    # serializer_class = HeroInfoModelSerializer
    pagination_class = LargeResultsSetPage #指定分页类 写你自定义的类对象
    permission_classes = [permissions.IsAuthenticated] #只有登录的用户才能访问的接口

    # http://127.0.0.1:8000/books/heros/?author=尤雨溪
    filter_fields  = ['author']  #配置要过滤的字段
    # http://127.0.0.1:8000/books/heros/?ordering_=-id  为降序
    filter_backends = [OrderingFilter, DjangoFilterBackend,]   #指定过滤后端为排序而不是过滤
    ordering_fields = ('id','name','author') #指定要排序的字段
    # 此处区分请求的方法
    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH','POST']:
            return HeroInfoModelSerializer
        if self.request.method == 'GET':
            strs = self.request.query_params
            for key,value in strs.items():
                print(key, value)
            return GetHeroInfoModelSerializer
            # logging.warning(re.findall(r'(?<==)\S+',strs))



