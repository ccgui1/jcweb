from django.db import models

# Create your models here.
class JCmeeting(models.Model):
    meeting_name = models.CharField(max_length=100,verbose_name="会议主题")
    start_time = models.DateField(verbose_name='会议日期')
    host_name = models.CharField(max_length=100,verbose_name="主讲人")
    meeting_number = models.CharField(max_length=200,verbose_name="会议人数")
    meeting_link = models.CharField(max_length=200,verbose_name="会议链接")


    class Meta:
        verbose_name = '建策会议信息表'
        verbose_name_plural = verbose_name
