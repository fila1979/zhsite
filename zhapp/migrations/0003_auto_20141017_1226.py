# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zhapp', '0002_auto_20141017_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navbarmenu',
            name='navbar_menu',
            field=models.CharField(max_length=50, verbose_name=b'\xd0\x93\xd0\xbb\xd0\xb0\xd0\xb2\xd0\xbd\xd0\xbe\xd0\xb5 \xd0\xbc\xd0\xb5\xd0\xbd\xd1\x8e'),
        ),
    ]
