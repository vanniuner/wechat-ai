#-*- coding: UTF-8 -*-
import sys
sys.path.append('../SDK')  
import optparse
import time
import apiutil
import base64
import ConfigParser

cf=ConfigParser.ConfigParser()
cf.read("config.prop")
app_key = cf.get('txopen','app_key')
app_id = cf.get('txopen','app_id')

if __name__ == '__main__':
    str_text = '今天天气晴'
    type = 0
    ai_obj = apiutil.AiPlat(app_id, app_key)
    rsp = ai_obj.getAaiTts(str_text)
    if rsp['ret'] == 0:
        f = open('test.wav', 'wb')
        f.write(base64.b64decode(rsp["data"]["speech"]))
        f.close()
    else:
        print 'API FAIL'

