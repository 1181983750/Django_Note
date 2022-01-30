#导入框架里的序列化器

from rest_framework import serializers
#导入booktest应用的数据表模型 导入表模型
from booktest import models
from booktest.models import BookInfo,HeroInfo
#写法一：表模型 序列化器
class BookInfoSerializer(serializers.ModelSerializer):
    """定义序列化器"""
    class Meta:
        model = BookInfo  #指定序列化器哪个表模型
        fields = '__all__'  #序列化哪些表字段 全部包括id
        # fields = ['id','bookname','price','author','publishing'] #指定要映射的字段
        # exclude = ['image'] # 除了image字段不映射，其余都要
        """注意! __all__下划线不能少"""
        # extra_kwargs = { # 修改字段参数
        #     'price': {'min_value':0,'required':True},
        #     'bcomment':{'min_value':0,'write_only':True}
        # }
        # read_only_fields = ['id','author','publishing']  #指定那些字段只做序列化 只读
        #depth = 1  #指定嵌套序列化深度



class HeroInfoSerializer(serializers.ModelSerializer):
    """定义序列化器"""
    class Meta:
        model = HeroInfo  #指定序列化器哪个表模型
        fields = '__all__'  #序列化哪些表字段
    """注意! __all__下划线不能少"""


# 写法二：自定义 序列化器
# class BookInfoSerializer(serializers.Serializer):
#     """定义序列化器"""
#     #库存选项
#     STORAGE_CHOICES=(
#         (0, '无'),
#         (1, '有')
#     )
#
#     id = serializers.IntegerField(label='ID',read_only=True)
#     bookname = serializers.CharField(label='书名',required=True)
#     price = serializers.FloatField(label='价格',required=False)
#     author = serializers.CharField(label='作者',required=False)
#     publishing = serializers.CharField(label='出版社',required=False)
#     storage = serializers.ChoiceField(label='库存',choices=STORAGE_CHOICES,default='1',required=False)
#     image = serializers.FileField(required=False)
#     #序列化查询 bookinfo表里
#     """自定义校验规则 反序列化用"""
#     # def validate_bookname(self,value): #方法后接_ 校验的字段
#     #     if 'django' not in value.lower(): #value.lower查看开头与结尾字符串是不是django
#     #         raise serializers.ValidationError("书名不是django") #raise 返回错误的信息  和return效果差不多
#     #     #返回值给validate校验
#     #     return value
#
#     """自定义联合校验规则 反序列化用"""
#     # def validate(self,attrs):
#     #     #对多个字段进行联合校验
#     #     #attrs：是前端传来的所有数据
#     #     bread = attrs['bread'] #阅读量
#     #     bcomment = attrs['bcomment'] #评论量
#     #     if bread < bcomment:
#     #         raise serializers.ValidationError('阅读量小于评论量')
#     #     return attrs
#
#     # 新增
#     def create(self, validated_data):
#         """
#         当序列化器调用save方法，如果当初创建序列化器对象是没有给instance传参数
#         validated_data 是得来反序列化校验后的字典数据
#         """
#         book = BookInfo.objects.create(**validated_data)  # 两个**等同于拆包 = 下面代码
#         return book #必须返回一个对象 实际执行book.save()方法
#
#     # 更新
#     def update(self, instance, validated_data):
#         """
#         根据提供的验证过的数据更新和返回一个已经存在的`app`实例。
#         instance:要修改的模型对象字段 创建序列化器 BookInfoSerializer(instance=book,data=data)
#         """
#         instance.bookname = validated_data.get('bookname', instance.bookname)
#         instance.price = validated_data.get('price', instance.price)
#         instance.author = validated_data.get('author', instance.author)
#         instance.publishing = validated_data.get('publishing', instance.publishing)
#         instance.storage = validated_data.get('storage', instance.storage)
#         instance.image = validated_data.get('image', instance.image)
#         instance.save()
#         return instance

# class HeroInfoSerializer(serializers.Serializer):
#     name = serializers.CharField(label='名字',required=True)
#     author = serializers.CharField(label='作者')
#     # temp = serializers.CharField(label='序列化器自定义字段') #虚拟化环境下可以使用 表模型不存在的字段
#     #因为bookname是外键字段 将自动关联bookinfo表主键的id字段 注意字段名字不要写错
#     # bookname = serializers.PrimaryKeyRelatedField(label='书名',queryset=BookInfo.objects.all())
#     #只能读取 序列化输出给前端
#     # bookname = serializers.PrimaryKeyRelatedField(label='书名',read_only=True)
#     #默认是关联模型的__str__方法返回值序列化出来
#     # bookname = serializers.StringRelatedField(label='书名',read_only=True)
#     #将bookinfo序列化器中的所有字段序列化出来
#     bookname = BookInfoSerializer(read_only=True)
#
#
#     #新增
#     def create(self, validated_data):
#         """
#         当序列化器调用save方法，如果当初创建序列化器对象是没有给instance传参数
#         validated_data 是得来反序列化校验后的字典数据
#         """
#         hero = HeroInfo.objects.create(**validated_data)
#         return hero  #必须返回一个对象 hero.save()方法
#
#
#     #更新
#     def update(self, instance, validated_data):
#         """
#         根据提供的验证过的数据更新和返回一个已经存在的`app`实例。
#         instance:要修改的模型对象字段 创建序列化器 BookInfoSerializer(instance=book,data=data)
#         """
#         request = self.context['request'] # self指的就是HeroInfoSerializer序列化器
#         instance.name = validated_data.get('name', instance.name)
#         instance.author = validated_data.get('author', instance.author)
#         instance.save()
#         return instance