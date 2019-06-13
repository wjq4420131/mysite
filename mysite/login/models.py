from django.db import models


# Create your models here.
class Userinfo(models.Model):
    username = models.CharField(max_length=20, verbose_name='用户名')
    password = models.CharField(max_length=20, verbose_name='密码')



    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = '用户信息'
