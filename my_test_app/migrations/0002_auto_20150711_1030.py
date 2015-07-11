# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_test_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='animal',
            field=models.CharField(default=b'Animal', max_length=20),
        ),
        migrations.AddField(
            model_name='animal',
            name='salutation',
            field=models.CharField(default=b'NoSalutation', max_length=20),
        ),
    ]
