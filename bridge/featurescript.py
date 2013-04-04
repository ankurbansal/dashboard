from django.utils import timezone
import urllib2
from xml.etree import ElementTree
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from features.models import Features
from realworldapps.models import RealWorldApp



    
    


def fetchFeaturesInfoAndPersist(request):
    FetchGameInfo()
    FetchFeatureInfo()
    return HttpResponse("Welcome to D Dashboard feature page") 
    

def FetchGameInfo():
    print 'in gameinfo'
    global gameList
    tree = ElementTree.parse('C:\Users\sakjain\Desktop\workspace\dashboard\dashboard\RealWorldApps.xml')
    print tree
    rootElem = tree.getroot()
    gameList=[]
    recurseGame(rootElem)
    for value in gameList:
        try:
            print value.realworldapp_name
            a=RealWorldApp.objects.get(realworldapp_name__iexact=value.realworldapp_name)
            print a
        except ObjectDoesNotExist:
            print "Either the entry or blog doesn't exist."
            value.save()
            
def FetchFeatureInfo():
    global featureList
    tree1 = ElementTree.parse('C:\Users\sakjain\Desktop\workspace\dashboard\dashboard\Features.xml')
    print tree1
    rootElem1 = tree1.getroot()
    featureList=[]
    recurseFeature(rootElem1)
    for value1 in featureList:
        try:
            print value1.featureName
            a1=Features.objects.get(featureName__iexact=value1.featureName)
            print a1
        except ObjectDoesNotExist:
            print "Either the entry or blog doesn't exist."
            value1.save()
    
def populateGameInfoObject(node):
    tmpObject= RealWorldApp();
    tmpObject.realworldapp_name=node.tag;
    tmpObject.cr_dt=timezone.now().date();
    tmpObject.deleted_flag=False;
    tmpObject.cr_user='SYSTEM'
    tmpObject.lst_dt=timezone.now().date();
    tmpObject.lst_user='SYSTEM'
    return tmpObject

def populateFeatureInfoObject(node):
    tmpObject= Features();
    tmpObject.featureName=node.tag;
    tmpObject.cr_dt=timezone.now().date();
    tmpObject.deleted_flag=False;
    tmpObject.cr_user='SYSTEM'
    tmpObject.lst_dt=timezone.now().date();
    tmpObject.lst_user='SYSTEM'
    return tmpObject


def recurseGame(node):
#    print val," ",node.tag,node.attrib
    if len(node._children)<=0:
        gameList.append(populateGameInfoObject(node));
        
    else:
        for i in xrange(0,len(node._children)):
            recurseGame(node._children[i])
            
def recurseFeature(node):
#    print val," ",node.tag,node.attrib
    if len(node._children)<=0:
        featureList.append(populateFeatureInfoObject(node));
        
    else:
        for i in xrange(0,len(node._children)):
            recurseFeature(node._children[i])
            