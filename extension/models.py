from django.db import models

# Create your models here.
class ExtensionJob(models.Model):
    extension_name = models.CharField(max_length=100,verbose_name="推广产品")
    extension_leader = models.CharField(max_length=100,verbose_name="负责人")
    extension_target = models.CharField(max_length=100,verbose_name="受众目标")
    start_time = models.DateField(verbose_name='开始推广时间')
    end_time = models.DateField(blank=True,null=True,verbose_name='结束推广时间')
    extension_effect = models.CharField(max_length=200,verbose_name="推广效果")

    class Meta:
        verbose_name = '建策市场推广'
        verbose_name_plural = verbose_name