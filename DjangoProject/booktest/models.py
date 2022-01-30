from django.db import models

# Create your models here.
STORAGE_CHOICES=(
        ('0', '无'),
        ('1', '有')
    )
class BookInfo(models.Model):
    #定义了一个name 字段   表模型定义为Char类型 长度32
    bookname = models.CharField( max_length=32 ,verbose_name='书名')
    #定义了一个name 字段   表模型定义为Char类型 长度64
    price = models.FloatField(max_length=32,verbose_name='价格')
    author = models.CharField(max_length=64,verbose_name='作者')
    #出版社
    publishing = models.CharField(max_length=64,verbose_name='出版社')
    #图片 如果表中已有数据，后续添加字段必须给默认值或为空，不然报错
    storage = models.CharField(choices=STORAGE_CHOICES,default='0',max_length=100,verbose_name='库存')
    # null 是针对数据库而言，如果 null = True, 表示数据库的该字段可以为空；blank 是针对表单的，
    # 如果 blank = True，表示你的表单填写该字段的时候可以不填，但是对数据库来说，没有任何影响
    image = models.ImageField(upload_to='book/', null=True,blank = True,verbose_name='封面图片')

    class Meta:
        verbose_name = "图书" #admin后台显示名字
        verbose_name_plural = verbose_name

    #定义了一个方法 返回一个字符串书名字段
    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.bookname


class HeroInfo(models.Model):
    # 定义了一个name 字段   表模型定义为Char类型 长度32
    name = models.CharField(max_length=32,verbose_name='人物名字')
    bookname = models.ForeignKey(BookInfo,on_delete=models.Case, verbose_name='书名') #外键
    author = models.CharField(max_length=64,verbose_name="作者")
    class Meta:
        verbose_name = "人物" #admin后台显示名字
        verbose_name_plural = verbose_name

"""
这里的语句相当于翻译成了mysql语句：
    create table app01_userinfo(
        id bigint auto_increment primary key  #主键 自增约束  就算Django没写也会自动生成
        name varchar(32),            
        password varchar(64),
        age int
"""

####        新建数据          ####
#UserInfo.objects.create(name="朱成聪",password=118198,age=15,sex='true',key=68.8)
#### 本质上相当于数据库执行 insert into app01_userinfo(name,password)values("朱成聪",118198)


####        删除数据          ####
#UserInfo.objects.filter(name="朱成聪",password=118198,age=15,sex='true',key=68.8).delete()
#### 本质上相当于数据库执行 insert into app01_userinfo(name,password)values("朱成聪",118198)