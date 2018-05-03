#!/bin/bash
git pull
ps -ef |grep wechat |awk '{print $2}'|xargs sudo kill -9
echo '' > nohup.out
nohup python wechat.py &
tail -f nohup.out
