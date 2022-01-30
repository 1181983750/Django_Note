from  rest_framework import serializers

from booktest.models import BookInfo, HeroInfo


#定义序列化器
class BookInfoModelSerializer(serializers.ModelSerializer):
    #定义一个属性选项
    class Meta:
        model = BookInfo #使用的数据表模型
        fields = '__all__' #全部字段都映射
        # depth = 1 #遍历显示深度
        # extra_kwargs = {  # 修改字段参数
        #     'storage': {'required': False},
        # }

class GetHeroInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroInfo  # 使用的数据表模型
        fields = '__all__'  # 全部字段都映射
        extra_kwargs = {  # 修改字段参数
            'bookname': {'read_only': False},
        }
        depth = 1 #只有get请求可以

class HeroInfoModelSerializer(serializers.ModelSerializer):
    #定义一个属性选项
    class Meta:
        model = HeroInfo #使用的数据表模型
        fields = '__all__' #全部字段都映射
        extra_kwargs = {   #修改字段参数
            'bookname': {'read_only':False},
            'author': {'required':False},
            'name': {'required': False},
        }
        # depth = 1 #只有get请求可以


    # def update(self, instance, validated_data):
    #  #     """
    #  #     根据提供的验证过的数据更新和返回一个已经存在的`app`实例。
    #  #     instance:要修改的模型对象字段 创建序列化器 BookInfoSerializer(instance=book,data=data)
    #  #     """
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.author = validated_data.get('author', instance.author)
    #     instance.bookname = validated_data.get('bookname', instance.bookname)
    #     instance.save()
    #     return instance

