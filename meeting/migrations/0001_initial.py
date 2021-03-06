# Generated by Django 3.1.2 on 2020-10-29 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JCmeeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_name', models.CharField(max_length=16, verbose_name='学生姓名')),
                ('start_time', models.DateField(verbose_name='会议日期')),
                ('host_name', models.CharField(max_length=100, verbose_name='主讲人')),
                ('meeting_number', models.CharField(max_length=200, verbose_name='会议人数')),
                ('meeting_link', models.CharField(max_length=200, verbose_name='会议链接')),
            ],
            options={
                'verbose_name': '建策会议信息表',
                'verbose_name_plural': '建策会议信息表',
            },
        ),
    ]
