# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comet', '0002_auto_20150730_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicator',
            name='outcomeArea',
            field=models.ForeignKey(blank=True, to='comet.OutcomeArea', null=True),
            preserve_default=True,
        ),
    ]
