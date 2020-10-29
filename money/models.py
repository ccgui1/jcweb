from django.db import models

# Create your models here.
class ConpanyMoney(models.Model):
    device_name = models.CharField(max_length=100,verbose_name="设备名称")
    buy_date = models.DateField(verbose_name="购置时间")
    buy_name = models.CharField(max_length=100,verbose_name="购置人")
    device_type = models.CharField(max_length=100,verbose_name="设备型号")
    device_number = models.CharField(max_length=100,verbose_name='购置数量')
    device_price = models.CharField(max_length=200,verbose_name="购置单价")


    class Meta:
        verbose_name = '公司资产管理'
        verbose_name_plural = verbose_name