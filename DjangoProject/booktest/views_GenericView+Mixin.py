from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.response import Response
from booktest.models import BookInfo
from booktest.serializer import BookInfoModelSerializer
#定义类 通用api视图 增加 查询全部
class BookListGenericAPIView(ListModelMixin,CreateModelMixin,GenericAPIView):
    #指定序列化器
    serializer_class = BookInfoModelSerializer
    #指定所有查询集
    queryset = BookInfo.objects.all()
    #这里的self.get_queryset()相当于BookInfo.objects.all()
    def get(self,request):
        # 继承ListModelMixin的方法 查询list
        return self.list(request)

    def post(self,request):
        # CreateModelMixin的方法  新增create
        return self.create(request)

#定义类 通用api视图 单个查询、修改、删除
class BookDetailGenericView(RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,GenericAPIView):
    serializer_class = BookInfoModelSerializer
    queryset = BookInfo.objects.all()
    #查询单一
    def get(self,request,pk):
        #继承RetrieveModelMixin 单一方法retrieve 查询
        return self.retrieve(request,pk)

    #修改单一
    def put(self,request,pk):
        #继承RetrieveModelMixin 单一方法 update 更新
        return self.update(request,pk)

    #删除单一
    def delete(self,request,pk):
        #继承RetrieveModelMixin 单一方法 destroy删除
        return self.destroy(request,pk)