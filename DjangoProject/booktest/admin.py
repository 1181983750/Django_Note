from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from booktest.models import BookInfo, HeroInfo  # . 表示同目录下的文件

# user = get_user_model()
# user.username
# 设置网站标签页头
admin.site.site_header = '羿诚书城管理系统'
# 设置页面标题
admin.site.site_title = '羿诚MIS'
# 设置首页标语
admin.site.index_title = '欢迎使用羿诚MIS'

class BookInfoAdmin(admin.ModelAdmin):
    actions_on_top = True
    actions_on_bottom = False
    list_display = ['id','bookname','price','author','storage','image']



class HeroInfoAdmin(admin.ModelAdmin):
    actions_on_top = True
    actions_on_bottom = False
    list_display = ['id', 'bookname', 'author']


# 注册表模型类 与定义的类
admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)
