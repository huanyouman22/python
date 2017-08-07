#!/usr/bin/python
#coding=utf-8
import rrdtool
import time

cur_time=str(time.time()) #获取当前linux的时间戳
rrd=rrdtool.create('Flow.rrd','--step','300','--start',cur_time,     #--step,300,设置5分钟一个数据点
	'DS:eth0_in:COUNTER:600:0;U',
	'DS:eth0_out:COUNTER:600:0;U',
	'RRA:AVERAGE:0.5:1:600',
	'RRA:AVERAGE:0.5:6:700',
	'RRA:AVERAGE:0.5:24:775',
	'RRA:AVERAGE:0.5:288:797',
	'RRA:MAX:0.5:1:600',
	'RRA:MAX:0.5:6:700',
	'RRA:MAX:0.5:24:775',
	'RRA:MAX:0.5:288:797',
	'RRA:MIN:0.5:1:600',
	'RRA:MIN:0.5:6:700',
	'RRA:MIN:0.5:24:775',
	'RRA:MIN:0.5:288:797',)
if rdd:
	print rrdtool.error()
