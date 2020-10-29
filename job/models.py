from django.db import models

# Create your models here.
class StudentJob(models.Model):
    student_id = models.IntegerField(verbose_name="学员编号")
    student_name = models.CharField(max_length=16,verbose_name="学生姓名")
    school_name = models.CharField(max_length=100,verbose_name="学校名字")
    start_time = models.DateField(verbose_name='就职时间')
    end_time = models.DateField(blank=True,null=True,verbose_name='离职时间')
    company_name = models.CharField(max_length=200,verbose_name="就职公司")
    job_name = models.CharField(max_length=80,verbose_name="就职岗位")

    class Meta:
        verbose_name = '学生就业信息表'
        verbose_name_plural = verbose_name