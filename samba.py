#!/usr/bin/python
import commands

def sambaService(content,sender):
    try:
        if content == "samba start":
            output = commands.getoutput("sudo mount /dev/sda /dev/t")
            sender.send(output)
            output = commands.getoutput("sudo /etc/init.d/samba restart")
            sender.send(output)
        if content == "samba stop":
            output = commands.getoutput("sudo /etc/init.d/samba stop")
            sender.send(output)
            output = commands.getoutput("sudo umount /dev/sda")
            sender.send(output)
    except Exception,e:
        sender.send("sth err")
