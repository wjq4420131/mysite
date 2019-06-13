# 作者：wjq   
# 创建时间: 2019/6/12  
# 文件: urls.py   
# 软件名称: PyCharm
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
]