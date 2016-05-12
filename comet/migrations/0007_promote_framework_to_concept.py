# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('aristotle_mdr', '0011_update_ckeditor_remove_d19_errors'),
        ('comet', '0006_auto_20160314_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='framework',
            name='created',
        ),
        migrations.RemoveField(
            model_name='framework',
            name='definition',
        ),
        migrations.RemoveField(
            model_name='framework',
            name='id',
        ),
        migrations.RemoveField(
            model_name='framework',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='framework',
            name='name',
        ),
        migrations.AddField(
            model_name='framework',
            name='_concept_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=None, serialize=False, to='aristotle_mdr._concept'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='framework',
            name='comments',
            field=ckeditor_uploader.fields.RichTextUploadingField(help_text='Descriptive comments about the metadata item.', blank=True),
        ),
        migrations.AddField(
            model_name='framework',
            name='origin_URI',
            field=models.URLField(help_text='If imported, the original location of the item', blank=True),
        ),
        migrations.AddField(
            model_name='framework',
            name='references',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AddField(
            model_name='framework',
            name='responsible_organisation',
            field=models.CharField(max_length=256, blank=True),
        ),
        migrations.AddField(
            model_name='framework',
            name='short_name',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='framework',
            name='submitting_organisation',
            field=models.CharField(max_length=256, blank=True),
        ),
        migrations.AddField(
            model_name='framework',
            name='superseded_by',
            field=models.ForeignKey(related_name='supersedes', blank=True, to='comet.Framework', null=True),
        ),
        migrations.AddField(
            model_name='framework',
            name='synonyms',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='framework',
            name='version',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
