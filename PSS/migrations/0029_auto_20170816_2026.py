# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-16 20:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PSS', '0028_total_for_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='total_for_admin',
            name='DM1',
            field=models.IntegerField(choices=[(1, 'YES'), (0, 'NO')], default=None),
        ),
        migrations.AddField(
            model_name='total_for_admin',
            name='DM10',
            field=models.IntegerField(choices=[(1, 'YES'), (0, 'NO')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='total_for_admin',
            name='DM11_1',
            field=models.IntegerField(choices=[(0, 'Worse'), (1, 'Same'), (2, 'Better'), (3, 'Do Not Know')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='total_for_admin',
            name='DM11_2',
            field=models.IntegerField(choices=[(0, 'Worse'), (1, 'Same'), (2, 'Better'), (3, 'Do Not Know')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='total_for_admin',
            name='DM11_3',
            field=models.IntegerField(choices=[(0, 'Worse'), (1, 'Same'), (2, 'Better'), (3, 'Do Not Know')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='total_for_admin',
            name='DM11_4',
            field=models.IntegerField(choices=[(0, 'Worse'), (1, 'Same'), (2, 'Better'), (3, 'Do Not Know')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='total_for_admin',
            name='DM12_1',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='total_for_admin',
            name='DM12_3',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='total_for_admin',
            name='DM13',
            field=models.IntegerField(choices=[(1, 'YES'), (0, 'NO')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='total_for_admin',
            name='DM14',
            field=models.IntegerField(choices=[(0, 'Native American or Alaska Native'), (1, 'Asian or Pacific Islande'), (2, 'Black or African American'), (3, 'White or European American'), (4, 'Non-White Hispanic'), (5, 'Bi- / multi-racial'), (6, 'Other')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='total_for_admin',
            name='DM14_1',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='total_for_admin',
            name='DM15',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='total_for_admin',
            name='DM16',
            field=models.IntegerField(choices=[(0, 'Less than High School'), (1, 'High-School / GED'), (2, 'Some College but no degree'), (3, 'Diploma or certificate from vocational, technical or trade school'), (4, 'Associates Degree'), (5, 'Bachelors Degree'), (6, 'Masters Degree'), (7, ' Professional School Degree'), (8, 'Doctorate')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='total_for_admin',
            name='DM17',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='total_for_admin',
            name='DM18',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='total_for_admin',
            name='DM19',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='total_for_admin',
            name='DM1_1_days',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='total_for_admin',
            name='DM1_1_month',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='total_for_admin',
            name='DM1_1_year',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='total_for_admin',
            name='DM1_2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='total_for_admin',
            name='DM1_3',
            field=models.IntegerField(choices=[(1, 'YES'), (0, 'NO')], default=0),
        ),
        migrations.AddField(
            model_name='total_for_admin',
            name='DM1_4',
            field=models.IntegerField(choices=[(1, 'YES'), (0, 'NO')], default=0),
        ),
        migrations.AddField(
            model_name='total_for_admin',
            name='DM2',
            field=models.IntegerField(choices=[(1, 'YES'), (0, 'NO')], default=0),
        ),
        migrations.AddField(
            model_name='total_for_admin',
            name='DM3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='total_for_admin',
            name='DM4',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='total_for_admin',
            name='DM5',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='total_for_admin',
            name='DM6',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='total_for_admin',
            name='DM7',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='total_for_admin',
            name='DM8',
            field=models.IntegerField(choices=[(0, 'Married, spouse present'), (1, 'Married, spouse absent'), (2, 'Never married'), (3, 'Sperated'), (4, 'Divorced'), (5, 'Widowed')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='total_for_admin',
            name='DM9',
            field=models.IntegerField(choices=[(0, 'Rental'), (1, 'Own home'), (2, 'Homeless'), (3, 'Public Housing'), (4, 'Other'), (5, 'Living with family or friend')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='total_for_admin',
            name='DM9_1',
            field=models.CharField(default='', max_length=200),
        ),
    ]
