from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _
from model_utils import Choices

from tinymce.models import HTMLField
import aristotle_mdr as aristotle

import importer

#CARDINALITY = Choices(('optional', _('Optional')),('conditional', _('Conditional')), ('mandatory', _('Mandatory')))
#class DataSetSpecification(managedObject):
#    template = "aristotle_mdr/dataSetSpecification.html"
#    def addDataElement(self,dataElement,**kwargs):
#        inc = DSSDEInclusion.objects.get_or_create(
#            dataElement=dataElement,
#            dss = self,
#            defaults = kwargs
#            )
#
#    @property
#    def registryCascadeItems(self):
#        return [i.dataElement for i in self.dataElements.all()]
#
#    @property
#    def getPdfItems(self):
#        des = self.dataElements.all()
#        return {
#            'dataElements':(de.dataElement for de in des),
#            #'dataElementConcepts':(de.dataElement.dataElementConcept for de in des),
#            'valueDomains':set(de.dataElement.valueDomain for de in des),
#            #'objectClasses':set(de.dataElement.dataElementConcept.objectClass for de in des),
#            #'properties':set(de.dataElement.dataElementConcept.property for de in des),
#        }
## Holds the link between a DSS and a Data Element with the DSS Specific details.
#class DSSDEInclusion(models.Model):
#    dataElement = models.ForeignKey(DataElement,related_name="dssInclusions")
#    dss = models.ForeignKey(DataSetSpecification,related_name="dataElements")
#    maximumOccurances = models.PositiveIntegerField(default=1)
#    cardinality = models.CharField(choices=CARDINALITY, default=CARDINALITY.conditional,max_length=20)
#    specificInformation = models.TextField(blank=True)
#    conditionalObligation = models.TextField(blank=True)
#    order = models.PositiveSmallIntegerField("Position",blank=True)
#    ordered = models.BooleanField(default=False)
#
#    class Meta:
#        verbose_name = "DSS Data Element Inclusion"

class IndicatorType(aristotle.models.concept):
    pass

# Subclassing from DataElement causes indicators to present as DataElements, which isn't quite right.
class Indicator(aristotle.models.concept):
    template = "comet/indicator.html"
    dataElementConcept = models.ForeignKey(aristotle.models.DataElementConcept,verbose_name = "Data Element Concept",blank=True,null=True)
    valueDomain = models.ForeignKey(aristotle.models.ValueDomain,verbose_name = "Value Domain",blank=True,null=True)

    indicatorType = models.ForeignKey(IndicatorType,blank=True,null=True)
    numerators = models.ManyToManyField(aristotle.models.DataElement,related_name="as_numerator")
    denominators = models.ManyToManyField(aristotle.models.DataElement,related_name="as_demoninator")
    disaggregators = models.ManyToManyField(aristotle.models.DataElement,related_name="as_disaggregator")

    numeratorText = models.TextField(blank=True)
    denominatorText = models.TextField(blank=True)
    computation = models.TextField(blank=True)
    computationDescription = HTMLField(blank=True)
    rationale = HTMLField(blank=True)
    disaggregationDescription = HTMLField(blank=True)

class IndicatorSetType(aristotle.models.unmanagedObject):
    pass

class IndicatorSet(aristotle.models.concept):
    template = "comet/indicatorset.html"
    indicators = models.ManyToManyField(Indicator,related_name="indicatorSets",blank=True,null=True)
    indicatorSetType = models.ForeignKey(IndicatorSetType,blank=True,null=True)

class OutcomeArea(aristotle.models.concept):
    pass

class QualityStatement(aristotle.models.concept):
    template = "comet/qualitystatement.html"
    timeliness  = HTMLField(blank=True)
    accessibility  = HTMLField(blank=True)
    interpretability  = HTMLField(blank=True)
    relevance  = HTMLField(blank=True)
    accuracy  = HTMLField(blank=True)
    coherence  = HTMLField(blank=True)
    implementationStartDate = models.DateField(blank=True,null=True)
    implementationEndDate = models.DateField(blank=True,null=True)

FREQUENCY = Choices( ('annually', _('Annually')),
        ('biannually', _('Biannually')),
        ('quarterly', _('Quarterly')),
        ('monthly', _('Monthly')),
        ('adhoc', _('Ad hoc')),
        ('notStated', _('Not stated')),
    )
class DataSource(aristotle.models.concept):
    template = "comet/datasource.html"
    qualityStatement = models.ForeignKey(QualityStatement,blank=True,null=True)
    linkToData = models.URLField(blank=True)
    custodian = models.TextField(max_length=256,blank=True)
    frequency = models.CharField(choices=FREQUENCY,default=FREQUENCY.notStated,max_length=20)

class Framework(aristotle.models.unmanagedObject):
    template = "comet/framework.html"
    parentFramework = models.ForeignKey('Framework',blank=True,null=True,related_name="childFrameworks")

def defaultData():
    print "Add aristotle defaults"
    aristotle.models.defaultData()
    indicatorTypes = [
       ("Indicator",""),
       ("Output measure",""),
       ("Progress measure",""),
       ]
    print "Adding indicator types"
    for name,desc in indicatorTypes:
        it,created = IndicatorType.objects.get_or_create(name=name,description=desc)
    indicatorSetTypes = [
       ("COAG-IGA","This includes indicators outlined in the Council of Australian government (COAG) Intergovernmental Agreement (IGA) on Federal Financial Relations relevant to national reporting on health, housing assistance and community services. The overall objective of these agreements is the improvement of the well-being of all Australians."),
       ("COAG-NP","The Council of Australian Governments (COAG) has agreed to a new form of payment called National Partnership (NP) payments to fund specific projects and to facilitate and/or reward States that deliver on nationally-significant reforms."),
       ("ROGS","The Review of Government Service Provision was established in 1993 by Heads of government (now the Council of Australian Governments or COAG) to provide information on the effectiveness and efficiency of government services in Australia. A Steering Committee, comprising senior representatives from the central agencies of all governments, manages the Review with the assistance of a Secretariat provided by the Productivity Commission."),
       ]
    print "Adding indicator set types"
    for name,desc in indicatorSetTypes:
        ist,created = IndicatorSetType.objects.get_or_create(name=name,description=desc)


def importMeteor():
    importer.importMeteor()
