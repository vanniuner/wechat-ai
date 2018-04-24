#!/usr/bin/python
import sys
sys.path.append("./project/RasWxNeteaseMusic")
from WxNeteaseMusic import WxNeteaseMusic
import ncmbot
from PluginManager import Model_MenuObj

wnm = WxNeteaseMusic()
ncmbot.login(phone='17302827960', password='7988860')

class MusicPlugin(Model_MenuObj):
    def __init__(self):
        pass

    def Start(content,sender):
    	if content.startswith("m"):
		    res = wnm.msg_handler(content)
		    sender.send(res)

