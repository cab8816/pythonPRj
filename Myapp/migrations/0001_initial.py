# Generated by Django 3.1.2 on 2020-10-30 13:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bpsdwxx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jyjcjgmc', models.CharField(default='检验检测机构名称', max_length=100, verbose_name='检验检测机构名称')),
                ('zcdz', models.CharField(default='注册地址', max_length=100, verbose_name='注册地址')),
                ('jydz', models.CharField(default='检验地址', max_length=100, verbose_name='检验地址')),
                ('yzbm', models.CharField(default='邮编', max_length=6, verbose_name='邮编')),
                ('chuanz', models.CharField(default='传真', max_length=20, verbose_name='传真')),
                ('email', models.CharField(default='email', max_length=50, verbose_name='email')),
                ('fzr', models.CharField(default='负责人', max_length=10, verbose_name='负责人')),
                ('fzrzw', models.CharField(default='负责人职务', max_length=20, verbose_name='负责人职务')),
                ('fzrgddh', models.CharField(default='负责人固定电话', max_length=20, verbose_name='负责人固定电话')),
                ('fzryddh', models.CharField(default='负责人移动电话', max_length=20, verbose_name='负责人移动电话')),
                ('llr', models.CharField(default='联络人', max_length=10, verbose_name='联络人')),
                ('llrzw', models.CharField(default='联络人职务', max_length=20, verbose_name='联络人职务')),
                ('llrgddh', models.CharField(default='联络人固定电话', max_length=20, verbose_name='联络人固定电话')),
                ('llryddh', models.CharField(default='联络人移动电话', max_length=20, verbose_name='联络人移动电话')),
                ('sfrdw', models.CharField(default='所属法人单位', max_length=100, verbose_name='所属法人单位')),
                ('sfrdwdz', models.CharField(default='法人单位地址', max_length=100, verbose_name='法人单位地址')),
            ],
            options={
                'verbose_name': '被评审单位信息表',
                'verbose_name_plural': '被评审单位信息表',
            },
        ),
        migrations.CreateModel(
            name='Pingshenxxb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pstzh', models.CharField(default='评审通知号', max_length=30, verbose_name='评审通知号')),
                ('jcjgmc', models.CharField(default='检测机构名称', max_length=100, verbose_name='检测机构名称')),
                ('psslh', models.CharField(default='受理号', max_length=50, verbose_name='受理号')),
                ('sqsx', models.CharField(default='申请事项', max_length=50, verbose_name='申请事项')),
                ('psdate', models.CharField(default='评审时间', max_length=30, verbose_name='评审时间')),
                ('psadress', models.CharField(default='评审地点', max_length=100, verbose_name='评审地点')),
                ('bpsdwxx', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Myapp.bpsdwxx', verbose_name='被评审单位Id')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户Id')),
            ],
            options={
                'verbose_name': '评审任务信息总表',
                'verbose_name_plural': '评审任务信息总表',
            },
        ),
        migrations.CreateModel(
            name='PsyuanDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8, verbose_name='姓名')),
                ('gender', models.CharField(max_length=4, verbose_name='性别')),
                ('danwei', models.CharField(max_length=100, verbose_name='工作单位')),
                ('psybh', models.CharField(max_length=15, verbose_name='评审员编号')),
            ],
            options={
                'verbose_name': '评审员个人信息表',
                'verbose_name_plural': '评审员个人信息表',
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, verbose_name='用户名')),
                ('realname', models.CharField(max_length=10, verbose_name='真名')),
            ],
            options={
                'verbose_name': '用户信息表',
                'verbose_name_plural': '用户信息表',
            },
        ),
        migrations.CreateModel(
            name='Xcpshcb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zhangbh', models.CharField(max_length=3, verbose_name='条款章号')),
                ('zhangmc', models.CharField(max_length=8, verbose_name='条款章名')),
                ('tkhao', models.CharField(max_length=10, verbose_name='条款号')),
                ('psneirong', models.CharField(max_length=1000, verbose_name='评审内容')),
                ('psjg', models.CharField(max_length=1, verbose_name='评审结果')),
                ('psyj', models.CharField(max_length=500, verbose_name='依据')),
                ('pssm', models.CharField(max_length=500, verbose_name='评审说明')),
            ],
            options={
                'verbose_name': '检验检测机构资质认定现场评审核查表',
                'verbose_name_plural': '检验检测机构资质认定现场评审核查表',
            },
        ),
        migrations.CreateModel(
            name='Xcpshcb71',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('psjd', models.CharField(max_length=1, verbose_name='不符合阶段')),
                ('psdate', models.DateField(auto_now=True, verbose_name='日期')),
                ('psjg', models.CharField(max_length=1, verbose_name='评审结果')),
                ('psyj', models.CharField(max_length=500, verbose_name='依据')),
                ('pssm', models.CharField(max_length=500, verbose_name='评审说明')),
                ('jzfs', models.CharField(max_length=1, verbose_name='纠正确认方式')),
                ('bsfyj', models.CharField(max_length=1, verbose_name='被评审方确认意见')),
                ('pszzyj', models.CharField(max_length=1, verbose_name='评审组长确认意见')),
                ('pshcxx', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Myapp.xcpshcb', verbose_name='核查信息')),
                ('psxxb', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Myapp.pingshenxxb', verbose_name='评审通知号')),
            ],
            options={
                'verbose_name': '现场评审核查表7.1',
                'verbose_name_plural': '现场评审核查表7.1',
            },
        ),
        migrations.CreateModel(
            name='Pszcy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('psyzc', models.CharField(max_length=10, verbose_name='评审员组成')),
                ('psname', models.CharField(max_length=10, verbose_name='姓名')),
                ('ziwuzicheng', models.CharField(max_length=30, verbose_name='职务/职称')),
                ('gzdw', models.CharField(max_length=50, verbose_name='工作单位')),
                ('lxfs', models.CharField(max_length=18, verbose_name='联系方式')),
                ('psxxbs', models.ManyToManyField(to='Myapp.Pingshenxxb', verbose_name='评审通知号')),
                ('psydtl', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Myapp.psyuandetail', verbose_name='评审员信息号')),
            ],
            options={
                'verbose_name': '评审组名单',
                'verbose_name_plural': '评审组名单',
            },
        ),
        migrations.AddField(
            model_name='pingshenxxb',
            name='userinfo',
            field=models.ManyToManyField(to='Myapp.UserInfo'),
        ),
        migrations.CreateModel(
            name='ImportFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('importtype', models.CharField(choices=[('0', '0_读取评审通知(docx格式)'), ('1', '1_读取评审报告(docx格式)'), ('3', '3_现场评审核查表(docx格式)'), ('2', '2_评审员信息表格(docx格式)')], default=0, max_length=1, verbose_name='导入类型')),
                ('file', models.FileField(upload_to='File', verbose_name='文件名')),
                ('psxxb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.pingshenxxb', verbose_name='评审信息ID')),
            ],
            options={
                'verbose_name': '从文件导入数据',
                'verbose_name_plural': '从文件导入数据',
            },
        ),
        migrations.CreateModel(
            name='Biao72',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xuhao', models.CharField(max_length=4, verbose_name='序号')),
                ('xmmc', models.CharField(max_length=100, verbose_name='检测类别项目或产品名称')),
                ('yjbz', models.CharField(max_length=300, verbose_name='依据标准及代号')),
                ('xmxh', models.CharField(max_length=20, verbose_name='参数序号')),
                ('csmc', models.CharField(max_length=100, verbose_name='参数名称')),
                ('yjbztk', models.CharField(max_length=300, verbose_name='标准条款号')),
                ('xcsy', models.BooleanField(default=False, verbose_name='现场试验')),
                ('nlyz', models.BooleanField(default=False, verbose_name='利用能力验证结果')),
                ('clsh', models.BooleanField(default=False, verbose_name='测量审核盲样试验')),
                ('bdjg', models.BooleanField(default=False, verbose_name='利用实验室间比对结果')),
                ('xcys', models.BooleanField(default=False, verbose_name='现场演示')),
                ('xctw', models.BooleanField(default=False, verbose_name='现场提问')),
                ('cyjlbg', models.BooleanField(default=False, verbose_name='查阅记录和报告')),
                ('hcyq', models.BooleanField(default=False, verbose_name='核查仪器设备配置')),
                ('sfqr', models.BooleanField(default=False, verbose_name='是否确认(Y/N)')),
                ('beizu', models.CharField(max_length=200, verbose_name='备注')),
                ('psxxb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.pingshenxxb')),
            ],
            options={
                'verbose_name': '现场评审能力确认方式及确认结果一览表 表7-2',
                'verbose_name_plural': '现场评审能力确认方式及确认结果一览表 表7-2',
            },
        ),
        migrations.CreateModel(
            name='Biao5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xuhao', models.CharField(max_length=2, verbose_name='序号')),
                ('name', models.CharField(max_length=10, verbose_name='姓名')),
                ('ziwuzicheng', models.CharField(max_length=30, verbose_name='职务/职称')),
                ('sqqzly', models.CharField(max_length=500, verbose_name='授权签字领域')),
                ('beizu', models.CharField(max_length=300, verbose_name='备注')),
                ('psxxb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.pingshenxxb')),
            ],
            options={
                'verbose_name': '建议批准的授权签字人 表5',
                'verbose_name_plural': '建议批准的授权签字人 表5',
            },
        ),
        migrations.CreateModel(
            name='Biao4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lyxh', models.CharField(max_length=20, verbose_name='领域序号')),
                ('lyname', models.CharField(max_length=100, verbose_name='领域')),
                ('lbxh', models.CharField(max_length=20, verbose_name='类别序号')),
                ('lb', models.CharField(max_length=100, verbose_name='类别')),
                ('dxxh', models.CharField(max_length=20, verbose_name='对象序号')),
                ('duixiang', models.CharField(max_length=100, verbose_name='检测对象')),
                ('xmxh', models.CharField(max_length=20, verbose_name='参数序号')),
                ('xmmc', models.CharField(max_length=100, verbose_name='参数名称')),
                ('csmc', models.CharField(max_length=100, verbose_name='参数名称')),
                ('yjbz', models.CharField(max_length=300, verbose_name='依据的标准（方法）名称及编号（含年号）')),
                ('xzfw', models.CharField(max_length=100, verbose_name='限制范围')),
                ('sm', models.CharField(max_length=200, verbose_name='说明')),
                ('psxxb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.pingshenxxb')),
            ],
            options={
                'verbose_name': '建议批准的检验检测能力表 表4',
                'verbose_name_plural': '建议批准的检验检测能力表 表4',
            },
        ),
    ]
