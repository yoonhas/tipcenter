# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-01 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PSS', '0016_auto_20170801_0601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='es',
            name='surveytime',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='exf',
            name='surveytime',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='f',
            name='surveytime',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='gd',
            name='surveytime',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='gr',
            name='surveytime',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='health',
            name='surveytime',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='hm',
            name='surveytime',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='r',
            name='surveytime',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sef',
            name='surveytime',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='spr',
            name='surveytime',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='ssp',
            name='surveytime',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tip',
            name='surveytime',
            field=models.IntegerField(),
        ),
    ]