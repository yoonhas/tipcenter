# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-02 05:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PSS', '0018_dm_dm_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dm',
            name='DM1',
            field=models.IntegerField(choices=[('YES', 1), ('NO', 0)], default=None),
        ),
        migrations.AlterField(
            model_name='dm',
            name='DM10',
            field=models.IntegerField(choices=[('YES', 1), ('NO', 0)]),
        ),
        migrations.AlterField(
            model_name='dm',
            name='DM13',
            field=models.IntegerField(choices=[('YES', 1), ('NO', 0)]),
        ),
        migrations.AlterField(
            model_name='dm',
            name='DM1_3',
            field=models.IntegerField(choices=[('YES', 1), ('NO', 0)], default=0),
        ),
        migrations.AlterField(
            model_name='dm',
            name='DM1_4',
            field=models.IntegerField(choices=[('YES', 1), ('NO', 0)], default=0),
        ),
        migrations.AlterField(
            model_name='dm',
            name='DM2',
            field=models.IntegerField(choices=[('YES', 1), ('NO', 0)], default=0),
        ),
    ]
