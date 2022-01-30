from rest_framework import status
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from booktest.models import BookInfo
from booktest.serializer import BookInfoModelSerializer


# 定义类 通用视图集
class BookViewSet(GenericViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer
    def list(self,request):
        # 序列化操作
        qs = self.get_queryset()
        serializer = self.get_serializer(instance=qs,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def create(self,request):
        serializer = BookInfoModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

   #单一增删改查
    def retrieve(self,request,pk):
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return Response({"message":"没有找到"},status=status.HTTP_404_NOT_FOUND)
        serializer = BookInfoModelSerializer(book)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def update(self,request,pk):
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return Response({"message":"没有找到"},status=status.HTTP_404_NOT_FOUND)
        serializer = BookInfoModelSerializer(instance=book,data=request.data,partial=True) #partial为只修改传来有值的部分
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

    def destroy(self,request,pk):
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return Response({"message":"没有找到"},status=status.HTTP_404_NOT_FOUND)
        book.delete()
        return Response({"message":"删除成功"},status=status.HTTP_204_NO_CONTENT)