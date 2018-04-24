#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'vanniuner'

import itchat
from itchat.content import *
import traceback
import commands
import sys
from PluginManager import PluginManager
from PluginManager import __ALLMODEL__

reload(sys)
sys.setdefaultencoding('utf-8')

global author
author=1

@itchat.msg_register([itchat.content.TEXT])
def wechat_onmessage(msg):
    if msg['Type'] == TEXT:
        output=""
        try:
            if msg['User'] and  u'\u6ce5\u4eba\u5f20' != msg['User']['NickName']:
                return 
            for SingleModel in __ALLMODEL__:
                plugins = SingleModel.GetPluginObject()
                for item in plugins:
                    item.Start(msg['Content'],author)
        except Exception,e:
            exstr = traceback.format_exc()
            print exstr
            print "sth error"

if __name__ == "__main__":
    PluginManager.LoadAllPlugin()
    itchat.auto_login(enableCmdQR=2, hotReload=True)
    author = itchat.search_friends(nickName=r'泥人张')[0]
    itchat.run()
