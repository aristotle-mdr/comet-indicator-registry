# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comet', '0004_auto_20160227_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicator',
            name='denominators',
            field=models.ManyToManyField(related_name='as_demoninator', to='aristotle_mdr.DataElement', blank=True),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='disaggregators',
            field=models.ManyToManyField(related_name='as_disaggregator', to='aristotle_mdr.DataElement', blank=True),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='numerators',
            field=models.ManyToManyField(related_name='as_numerator', to='aristotle_mdr.DataElement', blank=True),
        ),
    ]
