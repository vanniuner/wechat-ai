#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import commands
from PluginManager import Model_MenuObj
reload(sys)
sys.setdefaultencoding('utf-8')

global help_msg
help_msg = \
        u"H: 帮助信息\n" \
        u"M: 音乐\n" \
        u"BTC: 比特币\n" \
        u"EOS: EOS行情\n" \
        u"TM: 下载机\n" \
        u"SAM: SambaService start/stop\n"

class BtcPlugin(Model_MenuObj):
    def __init__(self):
        pass

    def Start(self,content,sender):
    	if content.startswith("h") == False:
    	    return
        sender.send(u'%s' % help_msg)
