# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('aristotle_mdr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Framework',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('name', models.TextField(help_text='The primary name used for human identification purposes.')),
                ('description', ckeditor.fields.RichTextField(help_text='Representation of a concept by a descriptive statement which serves to differentiate it from related concepts', verbose_name='definition')),
                ('parentFramework', models.ForeignKey(related_name='childFrameworks', blank=True, to='comet.Framework', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('_concept_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='aristotle_mdr._concept')),
                ('short_name', models.CharField(max_length=100, blank=True)),
                ('version', models.CharField(max_length=20, blank=True)),
                ('synonyms', models.CharField(max_length=200, blank=True)),
                ('references', ckeditor.fields.RichTextField(blank=True)),
                ('origin_URI', models.URLField(help_text='If imported, the original location of the item', blank=True)),
                ('comments', ckeditor.fields.RichTextField(help_text='Descriptive comments about the metadata item.', blank=True)),
                ('submitting_organisation', models.CharField(max_length=256, blank=True)),
                ('responsible_organisation', models.CharField(max_length=256, blank=True)),
                ('numeratorText', models.TextField(blank=True)),
                ('denominatorText', models.TextField(blank=True)),
                ('computation', models.TextField(blank=True)),
                ('computationDescription', ckeditor.fields.RichTextField(blank=True)),
                ('rationale', ckeditor.fields.RichTextField(blank=True)),
                ('disaggregationDescription', ckeditor.fields.RichTextField(blank=True)),
                ('dataElementConcept', models.ForeignKey(verbose_name='Data Element Concept', blank=True, to='aristotle_mdr.DataElementConcept', null=True)),
                ('denominators', models.ManyToManyField(related_name='as_demoninator', to='aristotle_mdr.DataElement')),
                ('disaggregators', models.ManyToManyField(related_name='as_disaggregator', to='aristotle_mdr.DataElement')),
            ],
            options={
                'abstract': False,
            },
            bases=('aristotle_mdr._concept',),
        ),
        migrations.CreateModel(
            name='IndicatorSet',
            fields=[
                ('_concept_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='aristotle_mdr._concept')),
                ('short_name', models.CharField(max_length=100, blank=True)),
                ('version', models.CharField(max_length=20, blank=True)),
                ('synonyms', models.CharField(max_length=200, blank=True)),
                ('references', ckeditor.fields.RichTextField(blank=True)),
                ('origin_URI', models.URLField(help_text='If imported, the original location of the item', blank=True)),
                ('comments', ckeditor.fields.RichTextField(help_text='Descriptive comments about the metadata item.', blank=True)),
                ('submitting_organisation', models.CharField(max_length=256, blank=True)),
                ('responsible_organisation', models.CharField(max_length=256, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('aristotle_mdr._concept',),
        ),
        migrations.CreateModel(
            name='IndicatorSetType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('name', models.TextField(help_text='The primary name used for human identification purposes.')),
                ('description', ckeditor.fields.RichTextField(help_text='Representation of a concept by a descriptive statement which serves to differentiate it from related concepts', verbose_name='definition')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IndicatorType',
            fields=[
                ('_concept_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='aristotle_mdr._concept')),
                ('short_name', models.CharField(max_length=100, blank=True)),
                ('version', models.CharField(max_length=20, blank=True)),
                ('synonyms', models.CharField(max_length=200, blank=True)),
                ('references', ckeditor.fields.RichTextField(blank=True)),
                ('origin_URI', models.URLField(help_text='If imported, the original location of the item', blank=True)),
                ('comments', ckeditor.fields.RichTextField(help_text='Descriptive comments about the metadata item.', blank=True)),
                ('submitting_organisation', models.CharField(max_length=256, blank=True)),
                ('responsible_organisation', models.CharField(max_length=256, blank=True)),
                ('superseded_by', models.ForeignKey(related_name='supersedes', blank=True, to='comet.IndicatorType', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('aristotle_mdr._concept',),
        ),
        migrations.CreateModel(
            name='OutcomeArea',
            fields=[
                ('_concept_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='aristotle_mdr._concept')),
                ('short_name', models.CharField(max_length=100, blank=True)),
                ('version', models.CharField(max_length=20, blank=True)),
                ('synonyms', models.CharField(max_length=200, blank=True)),
                ('references', ckeditor.fields.RichTextField(blank=True)),
                ('origin_URI', models.URLField(help_text='If imported, the original location of the item', blank=True)),
                ('comments', ckeditor.fields.RichTextField(help_text='Descriptive comments about the metadata item.', blank=True)),
                ('submitting_organisation', models.CharField(max_length=256, blank=True)),
                ('responsible_organisation', models.CharField(max_length=256, blank=True)),
                ('superseded_by', models.ForeignKey(related_name='supersedes', blank=True, to='comet.OutcomeArea', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('aristotle_mdr._concept',),
        ),
        migrations.CreateModel(
            name='QualityStatement',
            fields=[
                ('_concept_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='aristotle_mdr._concept')),
                ('short_name', models.CharField(max_length=100, blank=True)),
                ('version', models.CharField(max_length=20, blank=True)),
                ('synonyms', models.CharField(max_length=200, blank=True)),
                ('references', ckeditor.fields.RichTextField(blank=True)),
                ('origin_URI', models.URLField(help_text='If imported, the original location of the item', blank=True)),
                ('comments', ckeditor.fields.RichTextField(help_text='Descriptive comments about the metadata item.', blank=True)),
                ('submitting_organisation', models.CharField(max_length=256, blank=True)),
                ('responsible_organisation', models.CharField(max_length=256, blank=True)),
                ('timeliness', ckeditor.fields.RichTextField(blank=True)),
                ('accessibility', ckeditor.fields.RichTextField(blank=True)),
                ('interpretability', ckeditor.fields.RichTextField(blank=True)),
                ('relevance', ckeditor.fields.RichTextField(blank=True)),
                ('accuracy', ckeditor.fields.RichTextField(blank=True)),
                ('coherence', ckeditor.fields.RichTextField(blank=True)),
                ('implementationStartDate', models.DateField(null=True, blank=True)),
                ('implementationEndDate', models.DateField(null=True, blank=True)),
                ('superseded_by', models.ForeignKey(related_name='supersedes', blank=True, to='comet.QualityStatement', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('aristotle_mdr._concept',),
        ),
        migrations.AddField(
            model_name='indicatorset',
            name='indicatorSetType',
            field=models.ForeignKey(blank=True, to='comet.IndicatorSetType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='indicatorset',
            name='indicators',
            field=models.ManyToManyField(related_name='indicatorSets', null=True, to='comet.Indicator', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='indicatorset',
            name='superseded_by',
            field=models.ForeignKey(related_name='supersedes', blank=True, to='comet.IndicatorSet', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='indicator',
            name='indicatorType',
            field=models.ForeignKey(blank=True, to='comet.IndicatorType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='indicator',
            name='numerators',
            field=models.ManyToManyField(related_name='as_numerator', to='aristotle_mdr.DataElement'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='indicator',
            name='superseded_by',
            field=models.ForeignKey(related_name='supersedes', blank=True, to='comet.Indicator', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='indicator',
            name='valueDomain',
            field=models.ForeignKey(verbose_name='Value Domain', blank=True, to='aristotle_mdr.ValueDomain', null=True),
            preserve_default=True,
        ),
    ]
