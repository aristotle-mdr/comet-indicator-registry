from django import forms
from django.contrib import admin
from aristotle_mdr import admin as aristotle_admin # Must include 'admin' directly, otherwise causes issues.
import comet

#class DSSDEInclusionInline(admin.TabularInline):
#    model=MDR.DSSDEInclusion
#    extra=0
#    classes = ('grp-collapse grp-closed',)
#    raw_id_fields = ('dataElement',)
#    autocomplete_lookup_fields = {
#        'fk': ['dataElement']
#    }


#class DataSetSpecification(TrebleAdmin):
#    inlines = TrebleAdmin.inlines + [DSSDEInclusionInline, ]

class IndicatorAdmin(aristotle_admin.DataElementAdmin):
    fieldsets = aristotle_admin.DataElementAdmin.fieldsets + [
            ('Computation', {'fields': ['numerators','denominators']}),
    ]

class QualityStatementAdmin(aristotle_admin.ConceptAdmin):
    fieldsets = aristotle_admin.ConceptAdmin.fieldsets + [
            ('Data Quality Guidelines',
                {'fields': ['timeliness','accessibility','interpretability','relevance','accuracy','coherence']}),
            ('Implementation dates',
                {'fields': ['implementationStartDate','implementationEndDate']}),
    ]

class DataSourceAdmin(aristotle_admin.ConceptAdmin):
    fieldsets = aristotle_admin.ConceptAdmin.fieldsets + [
            ('Data Source',
                {'fields': ['linkToData','custodian','frequency','qualityStatement']}),
    ]

# Register your models here.
admin.site.register(comet.models.Indicator,IndicatorAdmin)
admin.site.register(comet.models.QualityStatement,QualityStatementAdmin)
admin.site.register(comet.models.DataSource,DataSourceAdmin)

