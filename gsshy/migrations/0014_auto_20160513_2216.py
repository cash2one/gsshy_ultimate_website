# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gsshy', '0013_researchcenterprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videoprofile',
            name='release_unit',
        ),
        migrations.DeleteModel(
            name='VideoProfile',
        ),
    ]
