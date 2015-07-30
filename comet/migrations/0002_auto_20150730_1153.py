# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comet', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='framework',
            old_name='description',
            new_name='definition',
        ),
        migrations.RenameField(
            model_name='indicatorsettype',
            old_name='description',
            new_name='definition',
        ),
    ]
