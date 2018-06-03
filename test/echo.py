#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import commands
from threading import Timer
sys.path.append('../project/py_aiplat/SDK')  
import optparse
import apiutil
import base64
import ConfigParser
import commands
reload(sys)
sys.setdefaultencoding('utf-8')

global intervaled
intervaled=60

global app_key
app_key = 1
global app_id
app_id = 1

def init():
    cf=ConfigParser.ConfigParser()
    cf.read("../project/py_aiplat/demo/config.prop")
    global app_key
    app_key = cf.get('txopen','app_key')
    global app_id
    app_id = cf.get('txopen','app_id')
def start(content):
    print "ok"
    print app_key
    print app_id
    if content.startswith("echo") == False:
        return
    str_text = content.replace("echo ","")
    ai_obj = apiutil.AiPlat(app_id, app_key)
    rsp = ai_obj.getAaiTts(str_text)
    print rsp['ret']
    if rsp['ret'] == 0:
        f = open('test.wav', 'wb')
        f.write(base64.b64decode(rsp["data"]["speech"]))
        f.close()
        res = commands.getoutput("omxplayer test.wav")
    else:
        res = 'API FAIL'
    print res
init()
start("echo ok")
