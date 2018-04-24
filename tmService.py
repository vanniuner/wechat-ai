#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import commands

reload(sys)
sys.setdefaultencoding('utf-8')

def tmService(content,sender):
    print content
    if content=="tm":
        res=commands.getoutput("transmission-remote -ne -l 2>&1 | sed '$d' | sed 's/[ ][ ]\+/,/g' | awk -F',' 'NR>1{print $2,$10\"\\n\"$9,$7\"kb\\n\"$4,$3}'")
    else:
        content = content.replace("tm","transmission-remote")
        res=commands.getoutput(content)
    sender.send(res)
