# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-03 22:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PSS', '0021_auto_20170802_2235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Total_for_Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Agent', models.IntegerField()),
                ('Time', models.IntegerField()),
                ('Date', models.DateField()),
                ('Health', models.IntegerField()),
                ('Community', models.IntegerField()),
                ('Childcare', models.IntegerField()),
                ('Jobskills', models.IntegerField()),
                ('SoftSkill', models.IntegerField()),
                ('Peb_all', models.IntegerField()),
                ('Empowerment', models.IntegerField()),
                ('Selfmotivation', models.IntegerField()),
                ('SkilResources', models.IntegerField()),
                ('GaolOrientation', models.IntegerField()),
                ('Ehs_all', models.IntegerField()),
                ('Ess1', models.IntegerField()),
                ('Ess2', models.IntegerField()),
                ('Ess3', models.IntegerField()),
                ('Ess4', models.IntegerField()),
                ('Ess_all', models.IntegerField()),
                ('PSS', models.IntegerField()),
                ('Resilience', models.IntegerField()),
                ('Self_Efficacy', models.IntegerField()),
                ('GR_Per', models.IntegerField()),
                ('GR_all', models.IntegerField()),
                ('SPR_all', models.IntegerField()),
                ('F_self', models.IntegerField()),
                ('F_other', models.IntegerField()),
                ('F_situation', models.IntegerField()),
                ('F_all', models.IntegerField()),
                ('caseNum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PSS.Surveyee')),
            ],
        ),
    ]
