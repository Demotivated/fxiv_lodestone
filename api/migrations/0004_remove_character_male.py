# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_character_male'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='male',
        ),
    ]
