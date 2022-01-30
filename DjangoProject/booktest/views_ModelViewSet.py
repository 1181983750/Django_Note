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


#导入框架的模型视图集
from rest_framework.viewsets import ModelViewSet
#导入booktest应用的数据表模型 导入表对象
from booktest.models import BookInfo, HeroInfo
# from booktest.serializer import BookInfoSerializer, HeroInfoSerializer
from booktest.serializer_demo import BookInfoSerializer, HeroInfoSerializer

"""
导入django  视图驱动类
接受Web请求并且返回Web响应 
响应可以是一张网页的HTML内容
一个重定向，一个404错误，一个JSON、XML文档，或者一张图片
"""



class BookInfoViewSet(ModelViewSet):
    """定义类视图"""
    #指定查询集 把数据表所有数据给这个对象
    queryset = BookInfo.objects.all()
    #指定序列化器
    serializer_class = BookInfoSerializer
    """这里的字符串放你序列化器的类名字"""

class HeroInfoViewSet(ModelViewSet):
    queryset = HeroInfo.objects.all()
    serializer_class = HeroInfoSerializer



"""
book = BookInfo.objects.get(id=6)
s = BookInfoSerializer(instance=book) #实例化序列化对象
logging.warning(s.data) #获取序列化后的数据
"""
# book = BookInfo.objects.get(id=1) #查询id为1的单条数据
# s = BookInfoSerializer(instance=book) #实例化序列化对象
# logging.error(s.data) #获取序列化后的数据

# bookqueryset = BookInfo.objects.all() #拿到bookinfo所有字段保存到查询集
# s1 = BookInfoSerializer(instance=bookqueryset,many=True) #实例化多个对象 所以many=True
# logging.error(s1.data)#获取序列化后的数据

"""
.data取得的数据是以下序列化格式
[
{},
{},
]
"""

"""序列化器 查询单个HeroInfo表里id为2的关联bookinfo表其他信息"""
# hero = HeroInfo.objects.get(id=2)
# hero.temp = '11' #序列化器可以增加表模型中不存在的字段
# h = HeroInfoSerializer(instance=hero)
# print(h.data)

"""序列化器 联立查询 查询HeroInfo表里id为1的数据 关联的是BookInfo表里的主键是多少"""
# hero = HeroInfo.objects.get(id=1) #查询条件
# select = HeroInfoSerializer(instance=hero) #instance传要查询的数据，如果有多个则需要many=True
# print(select.data) #data里的bookname字段为外键关联 bookinfo主键id

"""反序列化 存入数据库的过程"""
#模拟前端传来序列化数据
data={
    'bookname':'三国演义',
    'price':39.9,
    'author':'罗贯中',
    'publishing':'人民文学出版社'
}
#进行反序列化后存储到数据库
def post(request):
    serializer = BookInfoSerializer(data=data,context=request)
    serializer.is_valid() #必须调用 序列化器校验方法 返回True or False
    logging.error(serializer.errors) #获取校验错误信息
    print(serializer.validated_data) #获取反序列化校验成功数据
# serializer.save() #反序列化后存入数据库



