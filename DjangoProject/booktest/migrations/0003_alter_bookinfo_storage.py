# Generated by Django 3.2.9 on 2022-01-27 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0002_auto_20220127_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinfo',
            name='storage',
            field=models.CharField(choices=[('0', '无'), ('1', '有')], default='0', max_length=100, verbose_name='库存'),
        ),
    ]
