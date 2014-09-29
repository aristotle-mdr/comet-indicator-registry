from django.contrib import admin
from aristotle_mdr import admin as aristotle_admin # Must include 'admin' directly, otherwise causes issues.
import comet

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

# Register your models here.
admin.site.register(comet.models.Indicator,IndicatorAdmin)
admin.site.register(comet.models.QualityStatement,QualityStatementAdmin)