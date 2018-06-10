# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('cover', models.ImageField(upload_to='static/images/banner', verbose_name='轮播图')),
                ('link_url', models.URLField(max_length=150, verbose_name='图片链接')),
                ('idx', models.IntegerField(verbose_name='索引')),
                ('is_active', models.BooleanField(default=False, verbose_name='是否激活')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
            },
        ),
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(default='', max_length=30, verbose_name='分类名称')),
            ],
            options={
                'verbose_name': '博客分类',
                'verbose_name_plural': '博客分类',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('content', models.CharField(max_length=400, verbose_name='评论内容')),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='发布时间')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
        migrations.CreateModel(
            name='FriendlyLink',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=30, verbose_name='友情链接标题')),
                ('link', models.URLField(default=None, max_length=150, verbose_name='链接地址')),
            ],
            options={
                'verbose_name': '友情链接',
                'verbose_name_plural': '友情链接',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=30, verbose_name='标题')),
                ('content', models.CharField(max_length=4000, verbose_name='内容')),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='发布时间')),
                ('cover', models.ImageField(default=None, verbose_name='博客封面', upload_to='static/image/post')),
                ('views', models.IntegerField(verbose_name='浏览量')),
                ('is_recomment', models.BooleanField(default=False, verbose_name='是否推荐博客')),
                ('category', models.ForeignKey(default=None, to='blogs.BlogCategory', verbose_name='博客分类')),
            ],
            options={
                'verbose_name': '博客',
                'verbose_name_plural': '博客',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='标签')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='blogs.Tags', verbose_name='标签'),
        ),
    ]
