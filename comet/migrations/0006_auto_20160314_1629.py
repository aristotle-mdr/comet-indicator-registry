# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('comet', '0005_auto_20160227_2258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indicator',
            name='outcomeArea',
        ),
        migrations.AddField(
            model_name='framework',
            name='indicators',
            field=models.ManyToManyField(related_name='frameworks', null=True, to='comet.Indicator', blank=True),
        ),
        migrations.AddField(
            model_name='indicator',
            name='outcome_areas',
            field=models.ManyToManyField(related_name='indicators', null=True, to='comet.OutcomeArea', blank=True),
        ),
        migrations.AlterField(
            model_name='framework',
            name='definition',
            field=ckeditor_uploader.fields.RichTextUploadingField(help_text='Representation of a concept by a descriptive statement which serves to differentiate it from related concepts', verbose_name='definition'),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='comments',
            field=ckeditor_uploader.fields.RichTextUploadingField(help_text='Descriptive comments about the metadata item.', blank=True),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='computationDescription',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='disaggregation_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='rationale',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='references',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='indicatorset',
            name='comments',
            field=ckeditor_uploader.fields.RichTextUploadingField(help_text='Descriptive comments about the metadata item.', blank=True),
        ),
        migrations.AlterField(
            model_name='indicatorset',
            name='references',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='indicatorsettype',
            name='definition',
            field=ckeditor_uploader.fields.RichTextUploadingField(help_text='Representation of a concept by a descriptive statement which serves to differentiate it from related concepts', verbose_name='definition'),
        ),
        migrations.AlterField(
            model_name='indicatortype',
            name='comments',
            field=ckeditor_uploader.fields.RichTextUploadingField(help_text='Descriptive comments about the metadata item.', blank=True),
        ),
        migrations.AlterField(
            model_name='indicatortype',
            name='references',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='outcomearea',
            name='comments',
            field=ckeditor_uploader.fields.RichTextUploadingField(help_text='Descriptive comments about the metadata item.', blank=True),
        ),
        migrations.AlterField(
            model_name='outcomearea',
            name='references',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='qualitystatement',
            name='accessibility',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='qualitystatement',
            name='accuracy',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='qualitystatement',
            name='coherence',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='qualitystatement',
            name='comments',
            field=ckeditor_uploader.fields.RichTextUploadingField(help_text='Descriptive comments about the metadata item.', blank=True),
        ),
        migrations.AlterField(
            model_name='qualitystatement',
            name='interpretability',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='qualitystatement',
            name='references',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='qualitystatement',
            name='relevance',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='qualitystatement',
            name='timeliness',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]
