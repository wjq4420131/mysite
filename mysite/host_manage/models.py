from django.db import models


# Create your models here.
class Host(models.Model):
    name = models.CharField(max_length=125,verbose_name="主机名称")
    ip = models.CharField(max_length=125,verbose_name="主机ip")
    username = models.CharField(max_length=125,verbose_name="用户名")
    password = models.CharField(max_length=125,verbose_name="密码")
    port = models.IntegerField(max_length=22,verbose_name="端口")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural  = "主机表"
