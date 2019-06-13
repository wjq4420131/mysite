# 作者：wjq   
# 创建时间: 2019/6/10  
# 文件: forms.py   
# 软件名称: PyCharm
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
