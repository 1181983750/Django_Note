from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.response import Response
from rest_framework.utils import json
from booktest.models import BookInfo
from booktest.serializer import BookInfoModelSerializer
#定义类 通用api视图 增加 查询全部
class BookListGenericAPIView(ListCreateAPIView):
    #指定序列化器
    serializer_class = BookInfoModelSerializer
    #指定所有查询集
    queryset = BookInfo.objects.all()


#定义类 通用api视图 单个查询、修改、删除
class BookDetailGenericView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookInfoModelSerializer
    queryset = BookInfo.objects.all()
    #查询单一
