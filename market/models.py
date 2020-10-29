from django.db import models

# Create your models here.
class MarketFollow(models.Model):
    start_time = models.DateField(verbose_name='年份')
    thing_name = models.CharField(max_length=16,verbose_name="销售产品")
    leader_name = models.CharField(max_length=100,verbose_name="负责人")
    quarter_first = models.CharField(max_length=200,verbose_name="第一季度销售情况")
    quarter_second = models.CharField(max_length=200,verbose_name="第二季度销售情况")
    quarter_third = models.CharField(max_length=200,verbose_name="第三季度销售情况")
    quarter_forth = models.CharField(max_length=200,verbose_name="第四季度销售情况")



    class Meta:
        verbose_name = '建策销售情况'
        verbose_name_plural = verbose_name