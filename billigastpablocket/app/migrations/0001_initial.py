# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1000, null=True)),
                ('price', models.IntegerField(null=True)),
                ('category', models.CharField(max_length=500, null=True)),
                ('location', models.CharField(max_length=500, null=True)),
                ('downloaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
