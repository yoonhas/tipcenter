# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-01 19:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PSS', '0017_auto_20170801_0608'),
    ]

    operations = [
        migrations.CreateModel(
            name='DM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField()),
                ('surveytime', models.IntegerField()),
                ('DM1', models.IntegerField(choices=[(1, 'YES'), (0, 'NO')], default=None)),
                ('DM1_1_year', models.IntegerField(default=0)),
                ('DM1_1_month', models.IntegerField(default=0)),
                ('DM1_1_days', models.IntegerField(default=0)),
                ('DM1_2', models.IntegerField(default=0)),
                ('DM1_3', models.IntegerField(choices=[(1, 'YES'), (0, 'NO')], default=0)),
                ('DM1_4', models.IntegerField(choices=[(1, 'YES'), (0, 'NO')], default=0)),
                ('DM2', models.IntegerField(choices=[(1, 'YES'), (0, 'NO')], default=0)),
                ('DM3', models.IntegerField(default=0)),
                ('DM4', models.IntegerField(default=0)),
                ('DM5', models.IntegerField(default=0)),
                ('DM6', models.IntegerField(default=0)),
                ('DM7', models.IntegerField(default=0)),
                ('DM8', models.IntegerField(choices=[(0, 'Married, spouse present'), (1, 'Married, spouse absent'), (2, 'Never married'), (3, 'Sperated'), (4, 'Divorced'), (5, 'Widowed')])),
                ('DM9', models.IntegerField(choices=[(0, 'Rental'), (1, 'Own home'), (2, 'Homeless'), (3, 'Public Housing'), (4, 'Other'), (5, 'Living with family or friend')])),
                ('DM9_1', models.CharField(default='', max_length=200)),
                ('DM10', models.IntegerField(choices=[(1, 'YES'), (0, 'NO')])),
                ('DM11_1', models.IntegerField(choices=[(0, 'Worse'), (1, 'Same'), (2, 'Better'), (3, 'Do Not Know')])),
                ('DM11_2', models.IntegerField(choices=[(0, 'Worse'), (1, 'Same'), (2, 'Better'), (3, 'Do Not Know')])),
                ('DM11_3', models.IntegerField(choices=[(0, 'Worse'), (1, 'Same'), (2, 'Better'), (3, 'Do Not Know')])),
                ('DM11_4', models.IntegerField(choices=[(0, 'Worse'), (1, 'Same'), (2, 'Better'), (3, 'Do Not Know')])),
                ('DM12_1', models.IntegerField()),
                ('DM12_3', models.IntegerField()),
                ('DM13', models.IntegerField(choices=[(1, 'YES'), (0, 'NO')])),
                ('DM14', models.IntegerField(choices=[(0, 'Native American or Alaska Native'), (1, 'Asian or Pacific Islande'), (2, 'Black or African American'), (3, 'White or European American'), (4, 'Non-White Hispanic'), (5, 'Bi- / multi-racial'), (6, 'Other')])),
                ('DM14_1', models.CharField(default='', max_length=200)),
                ('DM15', models.IntegerField()),
                ('DM16', models.IntegerField(choices=[(0, 'Less than High School'), (1, 'High-School / GED'), (2, 'Some College but no degree'), (3, 'Diploma or certificate from vocational, technical or trade school'), (4, 'Associates Degree'), (5, 'Bachelors Degree'), (6, 'Masters Degree'), (7, ' Professional School Degree'), (8, 'Doctorate')])),
                ('DM17', models.IntegerField()),
                ('DM18', models.IntegerField()),
                ('DM19', models.IntegerField()),
                ('caseNum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PSS.Surveyee')),
            ],
        ),
        migrations.CreateModel(
            name='DM_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DM1', models.CharField(max_length=200)),
                ('DM1_1_year', models.CharField(max_length=200)),
                ('DM1_1_month', models.CharField(max_length=200)),
                ('DM1_1_days', models.CharField(max_length=200)),
                ('DM1_2', models.CharField(max_length=200)),
                ('DM1_3', models.CharField(max_length=200)),
                ('DM1_4', models.CharField(max_length=200)),
                ('DM2', models.CharField(max_length=200)),
                ('DM3', models.CharField(max_length=200)),
                ('DM4', models.CharField(max_length=200)),
                ('DM5', models.CharField(max_length=200)),
                ('DM6', models.CharField(max_length=200)),
                ('DM7', models.CharField(max_length=200)),
                ('DM8', models.CharField(max_length=200)),
                ('DM9', models.CharField(max_length=200)),
                ('DM9_1', models.CharField(max_length=200)),
                ('DM10', models.CharField(max_length=200)),
                ('DM11', models.CharField(max_length=200)),
                ('DM11_1', models.CharField(max_length=200)),
                ('DM11_2', models.CharField(max_length=200)),
                ('DM11_3', models.CharField(max_length=200)),
                ('DM11_4', models.CharField(max_length=200)),
                ('DM12', models.CharField(max_length=200)),
                ('DM12_1', models.CharField(max_length=200)),
                ('DM13', models.CharField(max_length=200)),
                ('DM14', models.CharField(max_length=200)),
                ('DM14_1', models.CharField(max_length=200)),
                ('DM15', models.CharField(max_length=200)),
                ('DM16', models.CharField(max_length=200)),
                ('DM17', models.CharField(max_length=200)),
                ('DM18', models.CharField(max_length=200)),
                ('DM19', models.CharField(max_length=200)),
            ],
        ),
    ]
