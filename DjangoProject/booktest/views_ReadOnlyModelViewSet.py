from rest_framework import status
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet

from booktest.models import BookInfo
from booktest.serializer import BookInfoModelSerializer


# 定义类 通用视图集
class BookViewSet(ReadOnlyModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer

""""
上面代码等于：
class BookViewSet(ListModelMixin,RetrieveModelMixin,GenericViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer
"""