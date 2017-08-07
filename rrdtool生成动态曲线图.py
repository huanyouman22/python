#!/usr/bin/python
#coding=utf-8

import rrdtool
import time

#定义图表上方大标题
title="sever network traffic flow ("+time.strftime('%Y-%m-%d',time.localtime(time.time()))+")"

rrdtool.graph("Flow.png","--start","-1d","--vertical-label=Bytes/s","--x-grid","MINUTE:12:HOUR:1HOUR:1:0:%H",\
	"--width","650","--height","230","--title",title,
	"DEF:inoctets=Flow.rr:etho_in:AVERAGE",
	"DEF:outoctets=Flow.rr:etho_out:AVERAGE",
	"CDEF:total=inoctets,outoctets,+",
	"LINE1:total#FF8833:Total traffic",
	"AREA:inoctets#00FF00:In traffic",
	"LINE1:outoctets#0000FF:Out traffic",
	"HRULE:6144#FF0000:Alarm value\\r",
	"CDEF:inbits=inoctets,8,*",
	"CDEF:outbits=outoctets,8,*",
	"COMMENT:\\r",
	"COMMENT:\\r",
	"GPRINT:inbits:AVERAGE:Avg In traffic\: %6.2lf %Sbps",
    "COMMENT: ",
    "GPRINT:inbits:MAX:Max In traffic\: %6.2lf %Sbps",
    "COMMENT: ",
    "GPRINT:inbits:MIN:Min In traffic\: %6.2lf %Sbps\\r",
    "COMMENT: ",
    "GPRINT:outbits:AVERAGE:Avg Out traffic\: %6.2lf %Sbps",
    "COMMENT: ",
    "GPRINT:outbits:MAX:Max out traffic\: %6.2lf %Sbps",
    "COMMENT: ",
    "GPRINT:outbits:MIN:Min out traffic\: %6.2lf %Sbps\\r")
