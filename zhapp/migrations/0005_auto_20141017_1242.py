# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zhapp', '0004_auto_20141017_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navbarmenu',
            name='navbar_menu',
            field=models.CharField(max_length=50, verbose_name='Введите новое категорию в меню'),
        ),
    ]
