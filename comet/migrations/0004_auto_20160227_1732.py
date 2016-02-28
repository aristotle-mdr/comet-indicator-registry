# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comet', '0003_indicator_outcomearea'),
    ]

    operations = [
        migrations.RenameField(
            model_name='indicator',
            old_name='denominatorText',
            new_name='denominator_description',
        ),
        migrations.RenameField(
            model_name='indicator',
            old_name='disaggregationDescription',
            new_name='disaggregation_description',
        ),
        migrations.RenameField(
            model_name='indicator',
            old_name='numeratorText',
            new_name='numerator_description',
        ),
        migrations.RemoveField(
            model_name='indicator',
            name='computation',
        ),
        migrations.AddField(
            model_name='indicator',
            name='denominator_computation',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='indicator',
            name='numerator_computation',
            field=models.TextField(blank=True),
        ),
    ]
