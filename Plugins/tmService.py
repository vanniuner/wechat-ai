#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import commands
from PluginManager import Model_MenuObj
reload(sys)
sys.setdefaultencoding('utf-8')

class TmPlugin(Model_MenuObj):
    def __init__(self):
        pass

    def Start(self,content,sender):
    	if content.startswith("tm") == False:
    		return
	if content=="tm":
            res=commands.getoutput("transmission-remote -ne -l 2>&1 | sed '$d' | sed 's/[ ][ ]\+/,/g' | awk -F',' 'NR>1{print $2,$10\"\\n\"$9,$7\"kb\\n\"$4,$3}'")
	else:
	    content = content.replace("tm","transmission-remote")
	    res=commands.getoutput(content)
	sender.send(res)
