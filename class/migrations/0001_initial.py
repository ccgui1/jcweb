# Generated by Django 3.1.2 on 2020-10-29 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=100, verbose_name='课程名')),
                ('class_type', models.CharField(max_length=100, verbose_name='课程类型')),
                ('class_time', models.DateField(verbose_name='课程时间')),
                ('class_teacher', models.DateField(verbose_name='授课老师')),
                ('class_number', models.CharField(max_length=200, verbose_name='上课人数')),
                ('class_link', models.CharField(blank=True, max_length=100, null=True, verbose_name='直播链接')),
            ],
            options={
                'verbose_name': '建策课堂管理',
                'verbose_name_plural': '建策课堂管理',
            },
        ),
    ]