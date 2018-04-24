#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'vanniuner'

import itchat
from itchat.content import *
import traceback
import commands
import sys
from threading import Timer
#from samba import sambaService
from music import musicService
from tmService import tmService

reload(sys)
sys.setdefaultencoding('utf-8')

global author
author=1

global intervaled
intervaled=60

global help_msg
help_msg = \
        u"H: 帮助信息\n" \
        u"M: 音乐\n" \
        u"BTC: 比特币\n" \
        u"TM: 下载机\n"


@itchat.msg_register([itchat.content.TEXT])
def wechat_onmessage(msg):
    if msg['Type'] == TEXT:
        output=""
        try:
            if msg['User'] and  u'\u6ce5\u4eba\u5f20' != msg['User']['NickName']:
                return 
            if msg['Content'] == 'h':
                global help_msg
                itchat.send(u'%s' % help_msg, msg['FromUserName'])
            elif msg['Content'].startswith("btc"):
                msg['Content'] = msg['Content'].replace("btc","btcprice")
                output=commands.getoutput(msg['Content'])
                itchat.send(u'%s' % output, msg['FromUserName'])
            # elif msg['Content'].startswith("samba"):
            #     sambaService(msg['Content'],author)
            elif msg['Content'].startswith("m"):
                musicService(msg['Content'][2:],author)
            elif msg['Content'].startswith("tm"):
                tmService(msg['Content'],author)
        except Exception,e:
            #exstr = traceback.format_exc()
            #print exstr
            print "sth error"

def timerfunc(inter,comm):
    try:
        Timer(inter, timerfunc, (inter,comm) ).start()
        global author
        output=commands.getoutput(comm)
        author.send(output)
    except Exception,e:
        print "timeout for btcprice service"

if __name__ == "__main__":
    Timer(intervaled, timerfunc, (intervaled,"btcprice -s USD,CNY -c 0.081932") ).start()
    itchat.auto_login(enableCmdQR=2, hotReload=True)
    author = itchat.search_friends(nickName=r'泥人张')[0]
    itchat.run()
