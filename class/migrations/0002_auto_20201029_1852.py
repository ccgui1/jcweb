# Generated by Django 3.1.2 on 2020-10-29 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classjob',
            name='class_teacher',
            field=models.CharField(max_length=100, verbose_name='授课老师'),
        ),
    ]