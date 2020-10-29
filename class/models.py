from django.db import models

# Create your models here.
class ClassJob(models.Model):
    class_name = models.CharField(max_length=100,verbose_name="课程名")
    class_type = models.CharField(max_length=100,verbose_name="课程类型")
    class_time = models.DateField(verbose_name='课程时间')
    class_teacher = models.CharField(max_length=100,verbose_name='授课老师')
    class_number = models.CharField(max_length=200,verbose_name="上课人数")
    class_link = models.CharField(blank=True,null=True,max_length=100,verbose_name="直播链接")

    class Meta:
        verbose_name = '建策课堂管理'
        verbose_name_plural = verbose_name