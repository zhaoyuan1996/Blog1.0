# @Time    : 18-6-5 下午2:19
# @Author  : zhaoyuan
# @Site    : 
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url
from .views import index, list1,base,show

urlpatterns = [
    url(r'^index/$', index, name='index'),
    url(r'^list/$',list1, name='list'),
    url(r'^base/$',base, name='base'),
    url(r'^show/$',show, name='show'),
    url(r'^tags(?P<tid>[0-9]+)/$',list1, name='tags'),
]
