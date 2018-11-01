from django.db import models


# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=32, verbose_name='名称')
    url = models.CharField(max_length=32, verbose_name='权限url')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name="父级菜单")

    class Meta:
        verbose_name = '权限'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=20, verbose_name='角色名称')
    permission = models.ManyToManyField(Menu, verbose_name='权限')

    class Meta:
        verbose_name = '角色'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
