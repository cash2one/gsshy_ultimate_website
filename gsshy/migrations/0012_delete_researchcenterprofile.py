# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gsshy', '0011_researchcenterprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ResearchCenterProfile',
        ),
    ]
