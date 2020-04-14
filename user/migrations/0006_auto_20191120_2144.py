# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-20 21:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20191120_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weibouser',
            name='access_token',
            field=models.CharField(db_index=True, max_length=32, verbose_name='微博授权密钥'),
        ),
        migrations.AlterField(
            model_name='weibouser',
            name='uid',
            field=models.CharField(db_index=True, max_length=10, verbose_name='微博uid'),
        ),
    ]