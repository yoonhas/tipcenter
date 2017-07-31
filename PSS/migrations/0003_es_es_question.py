# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-26 15:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PSS', '0002_eh_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='ES',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField()),
                ('ES1', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('ES2', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('ES3', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('ES4', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('ES5', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('ES6', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('ES7', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('ES8', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('ES9', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('ES10', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('ES11', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('ES12', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('ES13', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('ES14', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('ES15', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('caseNum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PSS.Surveyee')),
            ],
        ),
        migrations.CreateModel(
            name='ES_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EH1', models.CharField(max_length=200)),
                ('EH2', models.CharField(max_length=200)),
                ('EH3', models.CharField(max_length=200)),
                ('EH4', models.CharField(max_length=200)),
                ('EH5', models.CharField(max_length=200)),
                ('EH6', models.CharField(max_length=200)),
                ('EH7', models.CharField(max_length=200)),
                ('EH8', models.CharField(max_length=200)),
                ('EH9', models.CharField(max_length=200)),
                ('EH10', models.CharField(max_length=200)),
                ('EH11', models.CharField(max_length=200)),
                ('EH12', models.CharField(max_length=200)),
                ('EH13', models.CharField(max_length=200)),
                ('EH14', models.CharField(max_length=200)),
                ('EH15', models.CharField(max_length=200)),
            ],
        ),
    ]
