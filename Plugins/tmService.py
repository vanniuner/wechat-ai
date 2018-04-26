#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import commands
from threading import Timer
from PluginManager import Model_MenuObj
reload(sys)
sys.setdefaultencoding('utf-8')

global intervaled
intervaled=120

global tmcommand
tmcommand="transmission-remote -ne -l 2>&1 | sed '$d' | sed 's/[ ][ ]\+/,/g' | awk -F',' 'NR>1{print $2,$10\"\\n\"$9,$7\"kb\\n\"$4,$3}'"

def timerfunc(inter,comm):
    try:
        Timer(inter, timerfunc, (inter,comm) ).start()
        global authorg
        output=commands.getoutput(comm)
        authorg.send(output)
    except Exception,e:
        print "error for transmission service"

class TmPlugin(Model_MenuObj):
    def __init__(self):
        global tmcommand
        Timer(intervaled, timerfunc, (intervaled,tmcommand) ).start()

    def Start(self,content,sender):
    	if content.startswith("tm") == False:
    	    return
    	if content=="tm":
            global tmcommand
            res=commands.getoutput(rmcommand)
    	else:
    	    content = content.replace("tm","transmission-remote")
    	    res=commands.getoutput(content)
            sender.send(res)
