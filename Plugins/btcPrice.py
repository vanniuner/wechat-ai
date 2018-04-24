#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import commands
from threading import Timer
from PluginManager import Model_MenuObj
reload(sys)
sys.setdefaultencoding('utf-8')

global intervaled
intervaled=60

def timerfunc(inter,comm):
    try:
        Timer(inter, timerfunc, (inter,comm) ).start()
        global author
        output=commands.getoutput(comm)
        author.send(output)
    except Exception,e:
        print "timeout for btcprice service"

class BtcPlugin(Model_MenuObj):
    def __init__(self):
    	Timer(intervaled, timerfunc, (intervaled,"btcprice -s USD,CNY -c 0.081932 -m") ).start()
        pass

    def Start(content,sender):
    	if content.startswith("btc") == False:
            return
        res = content.replace("btc","btcprice -m")
	sender.send(res)
