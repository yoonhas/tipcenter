# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-07 22:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PSS', '0049_genb_genb_question_k6_k6_question_tipi_tipi_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='k6_question',
            name='Q2',
            field=models.CharField(max_length=300),
        ),
    ]
