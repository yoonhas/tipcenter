# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-26 16:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PSS', '0006_auto_20170726_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='EXF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField()),
                ('A3', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')], default=None)),
                ('B3', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')], default=None)),
                ('C3', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')], default=None)),
                ('D3', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')], default=None)),
                ('E2', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')], default=None)),
                ('F2', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')], default=None)),
                ('G1', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')], default=None)),
                ('H3', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')], default=None)),
                ('I2', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')], default=None)),
                ('J3', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')], default=None)),
                ('K1', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')], default=None)),
                ('K2', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')], default=None)),
                ('K3', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')], default=None)),
                ('L1', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')], default=None)),
                ('L2', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')], default=None)),
                ('L3', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')], default=None)),
                ('caseNum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PSS.Surveyee')),
            ],
        ),
        migrations.CreateModel(
            name='EXF_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('A3', models.CharField(max_length=200)),
                ('B3', models.CharField(max_length=200)),
                ('C3', models.CharField(max_length=200)),
                ('D3', models.CharField(max_length=200)),
                ('E2', models.CharField(max_length=200)),
                ('F2', models.CharField(max_length=200)),
                ('G1', models.CharField(max_length=200)),
                ('H3', models.CharField(max_length=200)),
                ('I2', models.CharField(max_length=200)),
                ('J3', models.CharField(max_length=200)),
                ('K1', models.CharField(max_length=200)),
                ('K2', models.CharField(max_length=200)),
                ('K3', models.CharField(max_length=200)),
                ('L1', models.CharField(max_length=200)),
                ('L2', models.CharField(max_length=200)),
                ('L3', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='F',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField()),
                ('F1', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], default=None)),
                ('F2', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], default=None)),
                ('F3', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], default=None)),
                ('F4', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], default=None)),
                ('F5', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], default=None)),
                ('F6', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], default=None)),
                ('F7', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], default=None)),
                ('F8', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], default=None)),
                ('F9', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], default=None)),
                ('F10', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], default=None)),
                ('F11', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], default=None)),
                ('F12', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], default=None)),
                ('F13', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], default=None)),
                ('F14', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], default=None)),
                ('F15', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], default=None)),
                ('F16', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], default=None)),
                ('F17', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], default=None)),
                ('F18', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], default=None)),
                ('caseNum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PSS.Surveyee')),
            ],
        ),
        migrations.CreateModel(
            name='F_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('F1', models.CharField(max_length=200)),
                ('F2', models.CharField(max_length=200)),
                ('F3', models.CharField(max_length=200)),
                ('F4', models.CharField(max_length=200)),
                ('F5', models.CharField(max_length=200)),
                ('F6', models.CharField(max_length=200)),
                ('F7', models.CharField(max_length=200)),
                ('F8', models.CharField(max_length=200)),
                ('F9', models.CharField(max_length=200)),
                ('F10', models.CharField(max_length=200)),
                ('F11', models.CharField(max_length=200)),
                ('F12', models.CharField(max_length=200)),
                ('F13', models.CharField(max_length=200)),
                ('F14', models.CharField(max_length=200)),
                ('F15', models.CharField(max_length=200)),
                ('F16', models.CharField(max_length=200)),
                ('F17', models.CharField(max_length=200)),
                ('F18', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='GD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField()),
                ('GD1', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], default=None)),
                ('GD2', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], default=None)),
                ('GD3', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], default=None)),
                ('GD4', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], default=None)),
                ('GD5', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], default=None)),
                ('GD6', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], default=None)),
                ('caseNum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PSS.Surveyee')),
            ],
        ),
        migrations.CreateModel(
            name='GD_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GD1', models.CharField(max_length=200)),
                ('GD2', models.CharField(max_length=200)),
                ('GD3', models.CharField(max_length=200)),
                ('GD4', models.CharField(max_length=200)),
                ('GD5', models.CharField(max_length=200)),
                ('GD6', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='GR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField()),
                ('GR1', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('GR2', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('GR3', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('GR4', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('GR5', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('GR6', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('GR7', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('GR8', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('caseNum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PSS.Surveyee')),
            ],
        ),
        migrations.CreateModel(
            name='GR_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GR1', models.CharField(max_length=200)),
                ('GR2', models.CharField(max_length=200)),
                ('GR3', models.CharField(max_length=200)),
                ('GR4', models.CharField(max_length=200)),
                ('GR5', models.CharField(max_length=200)),
                ('GR6', models.CharField(max_length=200)),
                ('GR7', models.CharField(max_length=200)),
                ('GR8', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='HEALTH',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField()),
                ('HEALTH1', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('HEALTH2', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('caseNum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PSS.Surveyee')),
            ],
        ),
        migrations.CreateModel(
            name='HEALTH_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HEALTH1', models.CharField(max_length=200)),
                ('HEALTH2', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='HM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField()),
                ('HM1', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('HM2', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('HM3', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('HM4', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('HM5', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('HM6', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('HM7', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('HM8', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('HM9', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('HM10', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('HM11', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('HM12', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('HM13', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('HM14', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('HM15', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('caseNum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PSS.Surveyee')),
            ],
        ),
        migrations.CreateModel(
            name='HM_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HM1', models.CharField(max_length=200)),
                ('HM2', models.CharField(max_length=200)),
                ('HM3', models.CharField(max_length=200)),
                ('HM4', models.CharField(max_length=200)),
                ('HM5', models.CharField(max_length=200)),
                ('HM6', models.CharField(max_length=200)),
                ('HM7', models.CharField(max_length=200)),
                ('HM8', models.CharField(max_length=200)),
                ('HM9', models.CharField(max_length=200)),
                ('HM10', models.CharField(max_length=200)),
                ('HM11', models.CharField(max_length=200)),
                ('HM12', models.CharField(max_length=200)),
                ('HM13', models.CharField(max_length=200)),
                ('HM14', models.CharField(max_length=200)),
                ('HM15', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='R',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField()),
                ('R1', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')], default=None)),
                ('R2', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')], default=None)),
                ('caseNum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PSS.Surveyee')),
            ],
        ),
        migrations.CreateModel(
            name='R_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('R1', models.CharField(max_length=200)),
                ('R2', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SEF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField()),
                ('SEF1', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('SEF2', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('SEF3', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('SEF4', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('SEF5', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('SEF6', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('SEF7', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('SEF8', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('caseNum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PSS.Surveyee')),
            ],
        ),
        migrations.CreateModel(
            name='SEF_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SEF1', models.CharField(max_length=200)),
                ('SEF2', models.CharField(max_length=200)),
                ('SEF3', models.CharField(max_length=200)),
                ('SEF4', models.CharField(max_length=200)),
                ('SEF5', models.CharField(max_length=200)),
                ('SEF6', models.CharField(max_length=200)),
                ('SEF7', models.CharField(max_length=200)),
                ('SEF8', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SPR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField()),
                ('SPR1', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=None)),
                ('SPR2', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=None)),
                ('SPR3', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=None)),
                ('SPR4', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=None)),
                ('SPR5', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=None)),
                ('SPR6', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=None)),
                ('caseNum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PSS.Surveyee')),
            ],
        ),
        migrations.CreateModel(
            name='SPR_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SPR1', models.CharField(max_length=200)),
                ('SPR2', models.CharField(max_length=200)),
                ('SPR3', models.CharField(max_length=200)),
                ('SPR4', models.CharField(max_length=200)),
                ('SPR5', models.CharField(max_length=200)),
                ('SPR6', models.CharField(max_length=200)),
                ('SPR7', models.CharField(max_length=200)),
                ('SPR8', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SSP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField()),
                ('SSP1', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], default=None)),
                ('SSP2', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], default=None)),
                ('SSP3', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], default=None)),
                ('SSP4', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], default=None)),
                ('SSP5', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], default=None)),
                ('SSP6', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], default=None)),
                ('SSP7', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], default=None)),
                ('SSP8', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], default=None)),
                ('SSP9', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], default=None)),
                ('SSP10', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], default=None)),
                ('SSP11', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], default=None)),
                ('SSP12', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], default=None)),
                ('caseNum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PSS.Surveyee')),
            ],
        ),
        migrations.CreateModel(
            name='SSP_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SSP1', models.CharField(max_length=200)),
                ('SSP2', models.CharField(max_length=200)),
                ('SSP3', models.CharField(max_length=200)),
                ('SSP4', models.CharField(max_length=200)),
                ('SSP5', models.CharField(max_length=200)),
                ('SSP6', models.CharField(max_length=200)),
                ('SSP7', models.CharField(max_length=200)),
                ('SSP8', models.CharField(max_length=200)),
                ('SSP9', models.CharField(max_length=200)),
                ('SSP10', models.CharField(max_length=200)),
                ('SSP11', models.CharField(max_length=200)),
                ('SSP12', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='eh',
            name='EH1',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=None),
        ),
        migrations.AlterField(
            model_name='eh',
            name='EH10',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=None),
        ),
        migrations.AlterField(
            model_name='eh',
            name='EH11',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=None),
        ),
        migrations.AlterField(
            model_name='eh',
            name='EH12',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=None),
        ),
        migrations.AlterField(
            model_name='eh',
            name='EH13',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=None),
        ),
        migrations.AlterField(
            model_name='eh',
            name='EH14',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=None),
        ),
        migrations.AlterField(
            model_name='eh',
            name='EH15',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=None),
        ),
        migrations.AlterField(
            model_name='eh',
            name='EH16',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=None),
        ),
        migrations.AlterField(
            model_name='eh',
            name='EH17',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=None),
        ),
        migrations.AlterField(
            model_name='eh',
            name='EH18',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=None),
        ),
        migrations.AlterField(
            model_name='eh',
            name='EH19',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=None),
        ),
        migrations.AlterField(
            model_name='eh',
            name='EH2',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=None),
        ),
        migrations.AlterField(
            model_name='eh',
            name='EH20',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=None),
        ),
        migrations.AlterField(
            model_name='eh',
            name='EH21',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=None),
        ),
        migrations.AlterField(
            model_name='eh',
            name='EH22',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=None),
        ),
        migrations.AlterField(
            model_name='eh',
            name='EH23',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=None),
        ),
        migrations.AlterField(
            model_name='eh',
            name='EH24',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=None),
        ),
        migrations.AlterField(
            model_name='eh',
            name='EH3',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=None),
        ),
        migrations.AlterField(
            model_name='eh',
            name='EH4',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=None),
        ),
        migrations.AlterField(
            model_name='eh',
            name='EH5',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=None),
        ),
        migrations.AlterField(
            model_name='eh',
            name='EH6',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=None),
        ),
        migrations.AlterField(
            model_name='eh',
            name='EH7',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=None),
        ),
        migrations.AlterField(
            model_name='eh',
            name='EH8',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=None),
        ),
        migrations.AlterField(
            model_name='eh',
            name='EH9',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=None),
        ),
    ]
