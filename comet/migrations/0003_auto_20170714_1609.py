# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('comet', '0002_indicatorsettype_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicator',
            name='denominators',
            field=models.ManyToManyField(related_name='as_denominator', to='aristotle_mdr.DataElement', blank=True),
        ),
        migrations.AlterField(
            model_name='indicatorsettype',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid1, help_text='Universally-unique Identifier. Uses UUID1 as this improves uniqueness and tracking between registries', unique=True, editable=False),
        ),
    ]
