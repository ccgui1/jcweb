from django.db import models

# Create your models here.
class TrainJob(models.Model):
    train_school = models.CharField(max_length=100,verbose_name="实训学校")
    train_class = models.CharField(max_length=100,verbose_name="实训班级")
    train_lesson = models.CharField(max_length=100,verbose_name="实训课程")
    start_time = models.DateField(verbose_name='实训开始时间')
    end_time = models.DateField(blank=True,null=True,verbose_name='实训结束时间')
    train_teacher = models.CharField(max_length=200,verbose_name="授课老师")
    train_leader = models.CharField(max_length=80,verbose_name="学校负责人")
    tel_number = models.CharField(max_length=80,verbose_name="联系方式")

    class Meta:
        verbose_name = '建策实训情况'
        verbose_name_plural = verbose_name