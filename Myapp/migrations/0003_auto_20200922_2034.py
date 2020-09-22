# Generated by Django 3.1.1 on 2020-09-22 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0002_auto_20200922_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importfile',
            name='importtype',
            field=models.CharField(choices=[('1', '1_读取评审报告(docx格式)'), ('3', '3_现场评审核查表(docx格式)'), ('0', '0_读取评审通知(docx格式)'), ('2', '2_评审员信息表格(docx格式)')], default=0, max_length=1, verbose_name='导入类型'),
        ),
    ]
