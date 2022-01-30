# Generated by Django 3.2.9 on 2022-01-28 07:02

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0006_alter_heroinfo_bookname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heroinfo',
            name='bookname',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.expressions.Case, to='booktest.bookinfo', verbose_name='书名'),
        ),
    ]
