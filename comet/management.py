from django.db.models import signals
from django.conf import settings
import comet
import aristotle_mdr

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

def loadTestData(**kwargs):
    print "Loading Comet test data because DEBUG is set to True."
    signals.post_save.disconnect(aristotle_mdr.models.concept_saved)
    comet.models.testData()
    signals.post_save.connect(aristotle_mdr.models.concept_saved)

if getattr(settings, 'DEBUG', "") == True:
    signals.post_syncdb.connect(loadTestData, sender=comet.models)