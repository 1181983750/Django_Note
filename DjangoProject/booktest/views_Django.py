"""
GET     /books/         查询全部记录
POST    /books/         新增一条记录
GET     /books/:id/     提供指定id记录
PUT     /books/:id/     修改指定id记录
DELETE  /books/:id/     删除指定id记录
JSON格式数据响应
:id  占位表示  实际传入查询的id
"""
import logging

from django.http import HttpResponse, JsonResponse
import json
#导入框架的模型视图集
from rest_framework.viewsets import ModelViewSet
#导入booktest应用的数据表模型 导入表对象
from booktest.models import BookInfo, HeroInfo
# from booktest.serializer import BookInfoSerializer, HeroInfoSerializer

"""
导入django  视图驱动类
接受Web请求并且返回Web响应 
响应可以是一张网页的HTML内容
一个重定向，一个404错误，一个JSON、XML文档，或者一张图片
"""

from django.views import View

#新增图书
class BookListAdd(View):
    def post(request):
        BookInfo.objects.create(bookname="Vue项目实战",price=98.5,author="尤雨溪",publishing="纽约大学出版社")
        return HttpResponse("数据插入成功")

#查询列表视图
class BookListView(View):
    def get(self,request):
        #查询所有图书接口
        #1.orm查询除所有图书模型 得到一堆对象
        books = BookInfo.objects.all()
        #2.遍历查询到的对象，取得对象里的每个字段
        # 定义一个数组列表 用来保存所有字典对象
        book_list = []
        for i in books:
            book_dict = {
                'bookname':i.bookname,
                'price':i.price,
                'author':i.author,
                'publishing':i.publishing
            }
            #相当于js push一个数组
            book_list.append(book_dict)
        """
        3.return 响应给前端 HttpResponse, JsonResponse都可以使用
        只不过Http的话传给前端需要json.dumps(res)传
        前端收到后需要js反序列化:res = JSON.parse(data);序列化JSON.stringify(res)
        JsonResponse里传一个safe=False是代表全部python格式都转JSON格式
        """
        return JsonResponse(book_list,safe=False)

    def post(self,request):
        #新增图书接口
        #获取前端传入的请求体数据（JSON）request.body
        json_str_bytes = request.body
        #把bytes类型的JSON字符串转换成json_str
        json_str = json_str_bytes.decode() #decode方法是转为字符串编码
        #利用json.loads将json字符串转换成json(字典or列表)
        book_dict = json.loads(json_str) #loads方法就是js的JSON.stringify()一样
        #创建模型对象并保存(把字典转换陈模型并存储)
        i = BookInfo(
            id=book_dict['id'],
            bookname = book_dict['bookname'],
            author = book_dict["author"],
            price = book_dict["price"],
            publishing = book_dict["publishing"]
        )
        i.save()
        #把新增模型转换为字典
        book_dict = {
            'id':i.id,
            'bookname': i.bookname,
            'price': i.price,
            'author': i.author,
            'publishing': i.publishing
        }
        #响应(把新增的数据在返回回去，201)
        return JsonResponse(book_dict,status=201)

#操作详情视图
class BookDetailView(View):
    def get(self,request,pk):
        #查询指定图书接口
        #1、获取指定id的那个模型对象
        try:
            i = BookInfo.objects.get(id=pk)
        #抛出异常  没查找到
        except BookInfo.DoesNotExist:
            #返回给前端一个JSON格式信息 并报一个状态码
            return HttpResponse({'message':'查询的数据不存在'},status=404)
        #2、模型对象转字典
        book_dict = {
            'bookname': i.bookname,
            'price': i.price,
            'author': i.author,
            'publishing': i.publishing
        }
        #3、响应
        return JsonResponse(book_dict)

    def put(self,request,pk):
        #修改所有图书接口
        #先查询要修改的模型对象
        try:
            i = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return JsonResponse({"message":"要修改的数据不存在"},status=404)
        #获取前端传入的新数据(把数据转换成字典)
        book_dict = json.loads(request.body.decode())
        #重新给模型指定属性赋值
        i.bookname = book_dict['bookname'] if book_dict['bookname'] != None else i.bookname
        i.price = book_dict['price'] if book_dict['price'] != None else i.price
        i.author = book_dict['author'] if book_dict['author'] != None else i.author
        i.publishing = book_dict['publishing'] if book_dict['publishing'] != None else i.publishing
        #调用save方法进行修改操作
        i.save()
        #把修改后的模型在转换诚字典
        edit_book_dict = {
            'bookname': i.bookname,
            'price': i.price,
            'author': i.author,
            'publishing': i.publishing
        }
        #返回响应给前端
        return JsonResponse(edit_book_dict)

    def delete(self,request,pk):
        #删除指定图书接口
        #获取要删除的模型对象
        try:
            i = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return JsonResponse({'message':"要删除的数据不存在"},status=404)
        #调用删除函数
        i.delete()
        #删除时不需要有响应体但是要返回给前端一个 204
        return JsonResponse({'message':"删除成功"},status=204)


