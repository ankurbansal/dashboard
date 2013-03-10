from django.utils import timezone
import urllib2
from xml.etree import ElementTree
from django.http import HttpResponse
from game.models import Game 
from django.core.exceptions import ObjectDoesNotExist

def fetchGameInfoAndPersist(request):
    global gameList

    tree = ElementTree.parse('C:\Users\sakshi\Documents\GitHub\dashboard\dashboard\Games.xml')
    print tree
    rootElem = tree.getroot()
    gameList=[]
    recurse(rootElem)
    for value in gameList:
        try:
            print value.game_name
            a=Game.objects.get(game_name__iexact=value.game_name)
            print a
        except ObjectDoesNotExist:
            print "Either the entry or blog doesn't exist."
            value.save()
    
    return HttpResponse("Welcome to D Dashboard Game page") 
    

    
def populateGameInfoObject(node):
    tmpObject= Game();
    tmpObject.game_name=node.tag;
    tmpObject.cr_dt=timezone.now().date();
    tmpObject.deleted_flag=False;
    tmpObject.cr_user='SYSTEM'
    tmpObject.lst_dt=timezone.now().date();
    tmpObject.lst_user='SYSTEM'
    return tmpObject


def recurse(node):
#    print val," ",node.tag,node.attrib
    if len(node._children)<=0:
        gameList.append(populateGameInfoObject(node));
        
    else:
        for i in xrange(0,len(node._children)):
            recurse(node._children[i])
            