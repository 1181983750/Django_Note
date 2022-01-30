# Generated by Django 3.2.9 on 2022-01-27 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinfo',
            options={'verbose_name': '图书', 'verbose_name_plural': '图书'},
        ),
        migrations.AlterModelOptions(
            name='heroinfo',
            options={'verbose_name': '人物', 'verbose_name_plural': '人物'},
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='author',
            field=models.CharField(max_length=64, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='bookname',
            field=models.CharField(max_length=32, verbose_name='书名'),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='image',
            field=models.ImageField(null=True, upload_to='book', verbose_name='封面图片'),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='price',
            field=models.FloatField(max_length=32, verbose_name='价格'),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='publishing',
            field=models.CharField(max_length=64, verbose_name='出版社'),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='storage',
            field=models.CharField(choices=[(0, '无'), (1, '有')], default='0', max_length=100, verbose_name='库存'),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='author',
            field=models.CharField(max_length=64, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='name',
            field=models.CharField(max_length=32, verbose_name='人物名字'),
        ),
    ]