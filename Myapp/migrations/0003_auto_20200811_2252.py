# Generated by Django 2.0 on 2020-08-11 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0002_auto_20200811_2248'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pstz',
            old_name='name',
            new_name='psname',
        ),
    ]
