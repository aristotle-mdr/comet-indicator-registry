from django.contrib import admin
import comet
from aristotle_mdr.register import register_concept

register_concept(comet.models.IndicatorSet)
register_concept(comet.models.OutcomeArea)

register_concept(comet.models.Indicator,
    extra_fieldsets = [
        ('Components', {'fields': ['dataElementConcept','valueDomain']}),
        ('Computation', {'fields': ['numerators','denominators']}),
        ]
    )


register_concept(comet.models.QualityStatement,
    extra_fieldsets = [
            ('Data Quality Guidelines',
                {'fields': ['timeliness','accessibility','interpretability','relevance','accuracy','coherence']}),
            ('Implementation dates',
                {'fields': ['implementationStartDate','implementationEndDate']}),
    ]
)

admin.site.register(comet.models.IndicatorSetType)
admin.site.register(comet.models.IndicatorType)

admin.site.register(comet.models.Framework)
