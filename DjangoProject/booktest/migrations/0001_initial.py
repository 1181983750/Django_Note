# Generated by Django 3.2.9 on 2022-01-24 14:46

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=32)),
                ('price', models.FloatField(max_length=32)),
                ('author', models.CharField(max_length=64)),
                ('publishing', models.CharField(max_length=64)),
                ('storage', models.CharField(choices=[(0, '无'), (1, '有')], default='有', max_length=100)),
                ('image', models.ImageField(null=True, upload_to='book', verbose_name='图书图⽚')),
            ],
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('author', models.CharField(max_length=64)),
                ('bookname', models.ForeignKey(on_delete=django.db.models.expressions.Case, to='booktest.bookinfo', verbose_name='书名')),
            ],
        ),
    ]