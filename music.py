#!/usr/bin/python
import sys
sys.path.append("./project/RasWxNeteaseMusic")
sys.path.append("./project/RasWxNeteaseMusic/neteaseApi/ncmbot")
from WxNeteaseMusic import WxNeteaseMusic
import ncmbot

wnm = WxNeteaseMusic()
ncmbot.login(phone='17302827960', password='7988860')
def musicService(content,sender):
    res = wnm.msg_handler(content)
    sender.send(res)

