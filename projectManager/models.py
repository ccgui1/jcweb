
from django.db import models

# Create your models here.
class PJManager(models.Model):
    projectManager_name = models.CharField(max_length=100,verbose_name="项目名称")
    projectManager_time = models.DateField(verbose_name='项目时间')
    projectMoney_name = models.CharField(max_length=100,verbose_name="项目出资方")
    Project_leader = models.CharField(max_length=200,verbose_name="项目负责人")
    Project_rate= models.CharField(max_length=200,verbose_name="项目完成进度")


    class Meta:
        verbose_name = '建策项目管理'
        verbose_name_plural = verbose_name
