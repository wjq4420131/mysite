# 作者：wjq   
# 创建时间: 2019/5/31  
# 文件: urls.py   
# 软件名称: PyCharm
from django.urls.conf import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:host_id>', views.delete, name='delete'),
]
