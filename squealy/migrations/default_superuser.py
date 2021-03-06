# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-01 06:42
from __future__ import unicode_literals

import os

from django.db import migrations
from django.contrib.auth.hashers import make_password

def create_default_superuser(apps, schema_editor):
    """
    Creates a default super user
    """
    User = apps.get_model('auth', 'user')
    username = os.environ.get('ADMIN_USERNAME', 'admin')
    password =  os.environ.get('ADMIN_PASS', 'admin@123')
    default_super_user = User(
        username=username,
        is_superuser=True,
        password=make_password(password),
        is_staff=True
    )
    default_super_user.save()

    Chart = apps.get_model('squealy', 'Chart')
    default_chart = Chart(
        name='Welcome To Squealy',
        url='welcome-to-squealy',
        query="""
    /*
    This is a sample report auto-generated by SQueaLy.
    ------------------------------------------------------

    Title - Worldwide Buisiness Analytics Market Share
    */
    SELECT  *
    FROM (
        VALUES
        ('SAP', 21),
        ('Oracle', 14),
        ('IBM', 13),
        ('SAS Institute', 12),
        ('Microsoft', 9),
        ('Others', 31)
        ) AS market_share (company, share);
    """,
        type='PieChart',
        options={
            "is3D": "true",
            "chartArea": {
                "width": "80%",
                "top": "10%",
                "height": "80%",
                "left": "5%"
            },
            "pieSliceText": "label",
            "width": 20,
            "title": "Worldwide Buisiness Analytics Market Share"
        }
    )
    default_chart.save()

    Validation = apps.get_model('squealy', 'Validation')
    default_validation = Validation(
        chart=default_chart,
        query="""
        /*This validation will pass
        if at least 1 row is returned.*/
        select 1,2,3 as "forcing_validation_pass";
        """,
        name='sample-validation'
    )
    default_validation.save()


class Migration(migrations.Migration):

    dependencies = [
        ('squealy', '0001_initial'),
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_superuser),
    ]
