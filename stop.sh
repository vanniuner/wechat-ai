#!/bin/bash
ps -ef |grep wechat |awk '{print $2}'|xargs sudo kill -9
