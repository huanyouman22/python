#!/usr/bin/python
#coding=utf-8

import rrdtool
import time,psutil

total_input_trafic = psutil.net_io_counters()[1]
total_output_travic = psutil.net_io_counter()[0]
starttime = int(time.time())

update=rrdtool.updateev('/home/test/rrdtool/Flow.rrd','%s %s %s') %(str(starttime),str(total_input_trafic),str(total_output_travic))
print update
