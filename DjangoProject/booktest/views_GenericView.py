from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.utils import json
from booktest.models import BookInfo
from booktest.serializer import BookInfoModelSerializer
#定义类 通用api视图 增加 查询全部
class BookListGenericAPIView(GenericAPIView):
    #指定序列化器
    serializer_class = BookInfoModelSerializer
    #指定所有查询集
    queryset = BookInfo.objects.all()
    #这里的self.get_queryset()相当于BookInfo.objects.all()
    def get(self,request):
        # 主要用来提供给Mixin扩展类使用，是列表视图与详情视图获取数据的基础
        qs = self.get_queryset()  #get_queryset返回视图使用的查询集，
        #返回序列化器对象get_serializer()相当于BookInfoModelSerializer(instance=queryset)
        serializer = self.get_serializer(instance=qs,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        data = request.data
        serializer = self.get_serializer(data=data)
        # 调用序列化器的is_valid方法进行校验 raise_exception有异常抛出异常
        serializer.is_valid(raise_exception=True)
        # 校验完成后调用序列化器的save方法进行执行数据库create方法
        serializer.save()
        # 因为反序列化会自动序列化 所以直接.data返回给前端序列化的数据
        return Response(serializer.data, status=status.HTTP_201_CREATED)

#定义类 通用api视图 单个查询、修改、删除
class BookDetailGenericView(GenericAPIView):
    serializer_class = BookInfoModelSerializer
    queryset = BookInfo.objects.all()

    #查询单一
    def get(self,request,pk):
        book = self.get_object() #相当于获取前端传来的要操作的pk等同于BookInfo.objects.get(id=pk)
        serializer = self.get_serializer(book)
        return Response(serializer.data)

    #修改单一
    def put(self,request,pk):
        try:
            book = self.get_object() #相当于获取前端传来的要操作的pk
        except BookInfo.DoesNotExist:
            return Response({'message':'没有找到'},status=status.HTTP_404_NOT_FOUND)
        data = request.data
        # partial为只修改传来有值的部分
        serializer = self.get_serializer(instance=book,data=data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    #删除单一
    def delete(self,request,pk):
        try:
            book = self.get_object() #相当于获取前端传来的要操作的pk
        except BookInfo.DoesNotExist:
            return Response({'message':'没有找到'},status=status.HTTP_404_NOT_FOUND)
        #取得当前查询到的对象 进行delete操作
        book.delete()
        return Response({'message':'删除成功'}, status=status.HTTP_204_NO_CONTENT)