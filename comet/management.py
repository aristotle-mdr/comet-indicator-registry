from django.db.models import signals
import comet

def create_indicator_types(app, created_models, verbosity, **kwargs):
    indicatorTypes = [
       ("Indicator",""),
       ("Output measure",""),
       ("Progress measure",""),
       ]
    print "Adding indicator types"
    for name,desc in indicatorTypes:
        comet.models.IndicatorType.objects.get_or_create(name=name,description=desc)

signals.post_syncdb.connect(create_indicator_types, sender=comet)
