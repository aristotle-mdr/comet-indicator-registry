# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from aristotle_mdr.utils.migrations import ConceptMigration

class Migration(ConceptMigration):

    dependencies = [
        ('comet', '0007_promote_framework_to_concept'),
        ('aristotle_mdr', '0013_concept_field_fixer_part1'),
    ]

    models_to_fix = [
        'indicator','indicatortype','indicatorset',
        'outcomearea','qualitystatement','framework'
    ]
