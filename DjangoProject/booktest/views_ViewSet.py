from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.viewsets import ViewSet

from booktest.models import BookInfo
from booktest.serializer import BookInfoModelSerializer


# 定义类 通用api视图
class BookViewSet(ViewSet):
    #增加 查询全部
    def list(self,request):
        # 指定所有查询集
        queryset = BookInfo.objects.all()
        # 序列化操作
        serializer = BookInfoModelSerializer(instance=queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


   #单一增删改查
    def retrieve(self,request,pk):
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return Response({"message":"没有找到"},status=status.HTTP_404_NOT_FOUND)
        serializer = BookInfoModelSerializer(book)
        return Response(serializer.data,status=status.HTTP_200_OK)


"""
路由
path("",bookviews.BookViewSet.as_view({'get':'list'})),

#get请求携带query的形参 http://127.0.0.1:8000/books/:ids   :ids是形参
path("<str:pk>" ,bookviews.BookViewSet.as_view({'get':'retrieve'})),
"""