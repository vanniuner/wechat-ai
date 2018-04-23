#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import commands

reload(sys)
sys.setdefaultencoding('utf-8')

def tmService(content,sender):
    if content=="tm":
        res=commands.getoutput("transmission-remote -l 2>&1 | sed '$d' | sed 's/[ ][ ]\+/,/g' | awk -F',' 'NR>1{print $2,$10\"\\n\"$9,$7\"kb\\n\"$4,$3}'")
        print res
    else:
        content = content.replace("tm","transmission-remote")
        res=commands.getoutput(content)
tmService("tm","user")
