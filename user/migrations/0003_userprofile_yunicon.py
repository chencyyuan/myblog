# Generated by Django 2.0 on 2019-05-08 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20190508_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='yunicon',
            field=models.CharField(default='', max_length=200),
        ),
    ]
