from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from booktest.models import BookInfo
from booktest.serializer import BookInfoModelSerializer
#定义类 api视图
class BookListAPIView(APIView):
    """ 查询视图  """
    def get(self,request):
        """查询所有"""
        queryset = BookInfo.objects.all()#从数据库拿到所有字段数据
        serializer = BookInfoModelSerializer(instance=queryset,many=True) #进行序列化，格式为json
        # print(serializer.data) #输出序列化后的数据
        res = Response(serializer.data)
        # print(res.data)#.data 响应对象 未渲染处理的数据
        # print(res.content) #处理后要响应给前端的数据
        return res#返回发送给前端序列化后的数据

    def post(self,request):
        """ 新增 """
        #获取前端传入的请求体数据
        data = request.data
        #创建序列化器进行反序列化 存入数据库
        serializer = BookInfoModelSerializer(data=data)
        #调用序列化器的is_valid方法进行校验 raise_exception有异常抛出异常
        serializer.is_valid(raise_exception=True)
        #校验完成后调用序列化器的save方法进行执行数据库create方法
        serializer.save()
        #因为反序列化会自动序列化 所以直接.data返回给前端序列化的数据
        return Response(serializer.data,status=status.HTTP_201_CREATED)

#定义类api视图
class BookDetailAPIView(APIView):
    #查询单一
    def get(self,request,ids):
        try:
            book = BookInfo.objects.get(id=ids)
        except BookInfo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        #创建序列化器进行序列化
        serializer = BookInfoModelSerializer(instance=book)
        #响应
        return Response(serializer.data,status=status.HTTP_200_OK)

    #修改单一
    def put(self,request,ids):
        try:
            book = BookInfo.objects.get(id=ids)
        except BookInfo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        #创建序列化器进行序列化 instance进行序列化读取，data进行反序列化存入数据库
        serializer = BookInfoModelSerializer(instance=book, data=request.data,partial=True)
        #调用序列化器的is_valid方法进行校验格式 raise_exception有异常抛出异常
        serializer.is_valid(raise_exception=True)
        #校验完成后调用序列化器的save方法进行执行数据库update方法
        serializer.save()
        #因为反序列化会自动序列化 所以直接.data返回给前端序列化的数据
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    #删除单一
    def delete(self,request,ids):
        try:
            book = BookInfo.objects.get(id=ids)
        except BookInfo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        #取得当前查询到的对象 进行delete操作
        book.delete()
        return Response({'message':'删除成功'}, status=status.HTTP_204_NO_CONTENT)