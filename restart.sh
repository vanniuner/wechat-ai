#!/bin/bash
#git pull
ps -ef |grep wechat |awk '{print $2}'|xargs sudo kill -9
python wechat.py
