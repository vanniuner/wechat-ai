#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import commands
from threading import Timer
from PluginManager import Model_MenuObj
reload(sys)
sys.setdefaultencoding('utf-8')

global intervaled
intervaled=30

global authorg
authorg=1

def timerfunc(inter,comm):
    try:
        Timer(inter, timerfunc, (inter,comm) ).start()
        global authorg
        output=commands.getoutput(comm)
        authorg.send(output)
    except Exception,e:
        print "timeout for btcprice service"

class BtcPlugin(Model_MenuObj):
    def __init__(self):
    	Timer(intervaled, timerfunc, (intervaled,"eos") ).start()

    def Start(self,content,sender):
        global authorg
        authorg = sender
    	if content.startswith("eos") == False:
            return
        res = commands.getoutput("eos")
	sender.send(res)
