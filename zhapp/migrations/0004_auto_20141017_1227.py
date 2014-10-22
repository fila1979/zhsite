# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zhapp', '0003_auto_20141017_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navbarmenu',
            name='navbar_menu',
            field=models.CharField(max_length=50, verbose_name='\u0413\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e'),
        ),
    ]
