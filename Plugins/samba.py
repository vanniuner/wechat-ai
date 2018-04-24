#!/usr/bin/python
import commands
from PluginManager import Model_MenuObj

class SambaPlugin(Model_MenuObj):
    def __init__(self):
        pass

    def Start(content,sender):
	    try:
	    	if content.startswith("samba"):
		        if content == "samba start":
		            output = commands.getoutput("sudo /etc/init.d/samba restart")
		            sender.send(output)
		        if content == "samba stop":
		            output = commands.getoutput("sudo /etc/init.d/samba stop")
		            sender.send(output)
	    except Exception,e:
	        sender.send("sth err")
