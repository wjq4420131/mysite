# 作者：wjq   
# 创建时间: 2019/5/31  
# 文件: urls.py   
# 软件名称: PyCharm
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'login'

urlpatterns = [
    path('', views.user_login, name='user_login'),
    #path('', auth_views.LoginView.as_view(template_name="login/login.html"), name='user_login'),
    #path('', auth_views.LogoutView.as_view, name='user_logout'),  # 使用Django内置的登出方法
    #path('delete/<int:user_id>', views.delete, name='delete'),
    path('', views.user_logout, name='user_logout'),
]
