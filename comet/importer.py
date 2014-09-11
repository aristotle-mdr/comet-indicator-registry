from lxml import etree
import aristotle_mdr as aristotle
import models
import datetime

METEOR_BASE = "http://meteor.aihw.gov.au/xmlapi3.0/items.phtml/clientId/jane/id/"

wg = None

touched=[]
tofetch= [489672,489630,481307,270263,268955,269231,269716,270807,287316,273050,489630] #IS,OC,P,DEC,VD,DE,DSS,I

def gtoe(xml,xpath):
    return getTextOrEmpty(xml,xpath)
def getTextOrEmpty(xml,xpath):
    text = xml.xpath(xpath)
    if len(text) > 0:
        text = text[0].text
        if text is not None:
            text = text.replace("&nbsp;",' ')
        else:
            text = ""
    else:
        text = ""
    return text
    
def importIndicators():
    parser = etree.XMLParser(encoding='utf-8')
    doc = etree.parse("http://meteor.aihw.gov.au/xmlapi3.0/list.phtml/clientId/jane/itemType/indicator",parser)
    items = doc.xpath('/list/identifier/meteorId/text()')
    for i in items:
        try:
            tofetch.append(int(i))
        except:
            pass
    importMeteor()

def importMeteor():
    global wg
    wg,c = aristotle.models.Workgroup.objects.get_or_create(name="Imported workgroup")
    for o in tofetch:
        getObject(o)

def getObject(meteorid):
    meteorid=str(meteorid)
    if meteorid in touched:
        print "Touched, ignoring - " + meteorid
        cls = aristotle.models._concept.objects.get_subclass(pk=meteorid)
        return cls

    print "Trying "+meteorid
    try:
        parser = etree.XMLParser(encoding='utf-8')
        doc = etree.parse(METEOR_BASE+str(meteorid),parser)
        touched.append(meteorid)
        items = doc.xpath('/items/*')
        if len(items) > 0:
            item = items[0]
            itemType = item.xpath('./identifier/itemType')[0].text
            load = { "property"    : loadProp,
                     "objectClass" : loadOC,
                     "dataElementConcept":loadDEC,
                     "dataElement":loadDE,
                     "valueDomain":loadVD,
                     "dataSetSpecification":loadDSS,
                     "indicator":loadInd,
                     "dataSource":loadDataSource,
                     #"indicatorSet":loadIS,
                }.get(itemType,None)
            if load is None:
                return None
            loaded = load(item)
            print "Loaded "+meteorid
            return loaded
    except:
        return None

def getStandard(item,tnType,requiredAttrs={}):
    std = {}
    fields=['name','meteorId']
    for i in fields:
        std[i]=gtoe(item,"./identifier/"+i)
    try:
        obj = tnType.objects.get(id=std['meteorId'])
        return obj
    except:
        pass
    syn = gtoe(item,"./indentifier/synonymousName")
    if std['meteorId']:
        obj,created = tnType.objects.get_or_create(id=std['meteorId'],workgroup=wg,**requiredAttrs)
    else:
        obj,created = tnType.objects.get_or_create(workgroup=wg,**requiredAttrs)
        # Damn data sources
    obj.name = std['name']
    description = gtoe(item,'./description') or gtoe(item,'./definition') or gtoe(item,'./identifier/description') or gtoe(item,'./indicatorDescription')
    if description:
        description += " <br><a href='http://meteor.aihw.gov.au/content/index.phtml/itemId/"+str(obj.id)+"'>Imported from Meteor</a>"
    else:
        description = "Description import failed!"
    obj.description = description 
    obj.shortName = gtoe(item,'./shortName')
    obj.references = gtoe(item,'./referenceDocuments')

    statesList = [aristotle.models.STATES[i] for i in range(len(aristotle.models.STATES))]

    for reg in item.xpath("./identifier/registrationStatus/status"):
        ra = reg.xpath("./registrationAuthority/name")[0].text
        print "registering "+std['meteorId']+" in "+ra

        ra,c=aristotle.models.RegistrationAuthority.objects.get_or_create(
                name=ra,description=ra +" authority")

        date = map(int,reg.xpath("date")[0].text.split("-"))
        status=reg.xpath("state")[0].text
        if status in statesList:
            state = statesList.index(status)
            ra.register(obj,state,datetime.date(*date))
    """
    """
    for rel in item.xpath("./relatedDataReferences/relatedDataReference"):
        relId = rel.xpath("identifier/meteorId")[0].text
        relType = rel.xpath("type")
        if len(relType) > 0:
            relType=relType[0].text
        else:
            relType=None
        if relType=="supersedes":
            print "Cascading into superseded object "+relId
            other = getObject(relId)
            if other:
                other.superseded_by = obj
                other.save()
        else:
            if relId not in touched:
                tofetch.append(relId)

    obj.save()
    return obj

def loadDE(de):
    dec=de.xpath("dataElementConcept/meteorId")
    if len(dec)>0:
        dec = dec[0].text
        try:
            dec = aristotle.models.DataElementConcept.objects.get(id=dec)
        except:
            dec = getObject(dec)
    else:
        dec=None
    vd=de.xpath("valueDomain/meteorId")
    if len(vd)>0:
        vd = vd[0].text
        try:
            vd = aristotle.models.ValueDomain.objects.get(id=vd)
        except:
            vd = getObject(vd)
    else:
        vd=None
    de = getStandard(de,aristotle.models.DataElement,
            {'dataElementConcept':dec,'valueDomain':vd})
    de.save()
    return de
def loadDEC(dec):
    p=dec.xpath("property/meteorId")
    if len(p)>0:
        p = p[0].text
        try:
            p = aristotle.models.Property.objects.get(id=p)
        except:
            p = getObject(p)
    else:
        p=None
    oc=dec.xpath("objectClass/meteorId")
    if len(oc)>0:
        oc = oc[0].text
        try:
            oc = aristotle.models.ObjectClass.objects.get(id=oc)
        except:
            oc = getObject(oc)
    else:
        oc=None
    dec = getStandard(dec,aristotle.models.DataElementConcept,{'property':p,'objectClass':oc})
    dec.save()
    return dec

def loadVD(vd):
    xml = vd
    #for dec in vd.xpath("./dataElementConcepts/identifier/meteorId"):
    #    tofetch.append(dec.text)

    vd = getStandard(vd,aristotle.models.ValueDomain,
            {   'maximumLength':int(gtoe(xml,"maximumCharacterLength")),
                'format':gtoe(xml,"format"),
                'dataType':aristotle.models.DataType.objects.get(name=gtoe(xml,"representationDatatype")),
                #'':,
            })
    gfu = gtoe(xml,"guideForUse")
    if gfu:
        vd.description += "<strong>Guide for use:</strong><br>"+gfu

    try:
        rc = gtoe(xml,"representationClass")
        vd.representationClass = aristotle.models.RepresentationClass.get(name=rc)
    except:
        pass
    vd.save()

    for pv in xml.xpath("./permissibleValues/valueDescriptor"):
        codeVal = aristotle.models.PermissibleValue(value=gtoe(pv,"value"),
            meaning=gtoe(pv,"meaning"),
            valueDomain=vd,order=1)
        codeVal.save()
    for sv in xml.xpath("./supplementaryValues/valueDescriptor"):
        codeVal = aristotle.models.SupplementaryValue(value=gtoe(sv,"value"),
            meaning=gtoe(sv,"meaning"),
            valueDomain=vd,order=1)
        codeVal.save()
    return vd
def loadOC(oc):
    for dec in oc.xpath("./dataElementConcepts/identifier/meteorId"):
        tofetch.append(dec.text)
    oc = getStandard(oc,aristotle.models.ObjectClass)
    oc.save()
    return oc
def loadProp(p):
    for dec in p.xpath("./dataElementConcepts/identifier/meteorId"):
        tofetch.append(dec.text)
    p = getStandard(p,aristotle.models.Property)
    p.save()
    return p

def loadDSS(dss):
    item = dss
    dss = getStandard(dss,aristotle.models.DataSetSpecification)
    dss.save()
    for i,de in enumerate(item.xpath("./contents/item[identifier/itemType='dataElement']")):
        de_id=de.xpath("./identifier/meteorId")[0].text
        obligation = de.xpath("./obligation")[0].text
        if obligation == "mandatory":
            obligation = aristotle.models.CARDINALITY.mandatory
        elif obligation == "optional":
            obligation = aristotle.models.CARDINALITY.optional
        else:
            obligation = aristotle.models.CARDINALITY.conditional
        maxOccurs = de.xpath("./maximumOccurrences")[0].text
        try:
            maxOccurs = int(maxOccurs)
        except:
            maxOccurs = 0
        try:
            deO = aristotle.models.DataElement.objects.get(id=de_id)
        except:
            deO = getObject(de_id)
        if deO:
            dss.addDataElement(deO,maximumOccurances=maxOccurs,
                specificInformation=gtoe(de,"./otherDatasetSpecificInformation"),
                cardinality=obligation,
                order=i,
                conditionalObligation=gtoe(de,"./conditionalObligation")
                )
    dss.description = dss.description + gtoe(item,"./comments")
    dss.save()
    return dss

def loadInd(ind):
    indi = getStandard(ind,models.Indicator)
    indi.numeratorText = gtoe(ind,"./numeratorHtml")
    indi.denominatorText = gtoe(ind,"./denominatorHtml")
    indi.computation = gtoe(ind,"./computation")
    indi.computationDescription = gtoe(ind,"./computationDescription")
    indi.disaggregationDescription = gtoe(ind,"./disaggregationHtml")
    indi.save()

    numer=ind.xpath("./numeratorElements//dataElement/meteorId")
    for n in numer:
        n=n.text
        try:
            de = aristotle.models.DataElement.objects.get(id=n)
        except:
            de = getObject(n)
        if de:
            indi.numerators.add(de)
    denom=ind.xpath("./denominatorElements//dataElement/meteorId")
    for d in denom:
        d=d.text
        try:
            de = aristotle.models.DataElement.objects.get(id=n)
        except:
            de = getObject(d)
        if de:
            indi.denominators.add(de)
    disagg=ind.xpath("./disaggregationElements//dataElement/meteorId")
    for d in disagg:
        d=d.text
        try:
            de = aristotle.models.DataElement.objects.get(id=n)
        except:
            de = getObject(d)
        if de:
            indi.disaggregators.add(de)
    try:
        it = gtoe(xml,"indicatorType")
        it = {  "pi":"Indicator",
                "om":"Output measure",
                "pm":"Progress measure"}[it]
        indi.indicatorType = models.IndicatorType.get(name=it)
    except:
        pass
    indi.save()
    print "indicator done"
    return indi

def loadFramework(f):
    pass

def loadDataSource(ds):
    item = getStandard(ds,models.DataSource)
    try:
        item.frequency = models.FREQUENCY[gtoe(ds,"./frequency").lower()]
    except:
        pass
    item.custodian = gtoe(ds,"./dataCustodian")
    return item
