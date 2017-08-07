#!/usr/bin/python
#coding=utf-8
from multiprocessing import cpu_count
import psutil
import sys
import os
import time
import atexit
import platform
import socket
import fcntl
import struct
import time
import MySQLdb

#print "welcome,current systerm is",os.name,"3 seconds late start to get data"
#time.sleep(3)
#line_num = 1

#funtion of platform,python的platform模块是收集系统信息的，os是相当于系统命令的
def os_detail():
	os_system = platform.uname()[0]
	os_hostname = platform.uname()[1]
	os_version = platform.uname()[2]
	return "系统："+str(os_system)"主机名："+str(os_hostname)+"os_version"+str(so_version)

	 
#function of GET CPU state，core为cpu的核数
def getCPUstate(interval=1):
	core = psutil.cpu_count()
	cpu_percent = "cpu"+str(psutil.cpu_percent(interval)+"%"
	return core

# function of GET Memory,显示可用内存信息
def getMemorystate():
	mem = psutil.virtual_memory()
	mem_total = str(int(mem.toal/1024/1024)+"M")
	mem_used = str(int(mem.used/1024/1024)+"M")
	mem_free = str(int(mem.free/1024/1024)+"M")
	mem_buffer = str(int(mem.buffers/1024/1024)+"M")
	mem_cache = str(int(mem.total*2/1024/1024)+"M")	

# function of 
# python中enumerate()会遍历牵引和元素
# python中reversed()函数是返回序列seq的反向访问的迭代子。反向排序
def bytes2human(n):      
        """    
        >>> bytes2human(10000)    
        '9.8 K'    
        >>> bytes2human(100001221)    
        '95.4 M'    
        """      
        symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')      
        prefix = {}      
        for i, s in enumerate(symbols):      
                prefix[s] = 1 << (i+1)*10      
        for s in reversed(symbols):      
                if n >= prefix[s]:      
                        value = float(n) / prefix[s]      
                        return '%.2f %s' % (value, s)      
        return '%.2f B' % (n)


# function of disk
#psutil.disk_partitions()
#[sdiskpart(device='/dev/sda3', mountpoint='/', fstype='ext4', opts='rw'),
# sdiskpart(device='/dev/sda1', mountpoint='/boot', fstype='ext4', opts='rw'), 
# sdiskpart(device='/dev/sr0', mountpoint='/yum', fstype='iso9660', opts='ro')]
# psutil.disk_usage("/")
#显示磁盘信息
def disk_detail():
	disk_num = len(psutil.disk_partitions())
	p = psutil.disk_partitions()
    for i in range(disk_num):
		device = {}
		x=p[i].device
		y=p[i].mountpoint
		device.append(x:y)
    
    return str(device)
#fidk_detail()


#psutil.net_io_counters()指的是网络连接信息
def poll(interval):      
    """Retrieve raw stats within an interval window."""      
    tot_before = psutil.net_io_counters()      
    pnic_before = psutil.net_io_counters(pernic=True)      
    # sleep some time      
    time.sleep(interval)      
    tot_after = psutil.net_io_counters()      
    pnic_after = psutil.net_io_counters(pernic=True)      
    # get cpu state      
    cpu_state = getCPUstate(interval)      
    # get memory      
    memory_state = getMemorystate()      
    return (tot_before, tot_after, pnic_before, pnic_after,cpu_state,memory_state)

#function of IP

def GetIP():
	outnet_IP = socket.gethostbyname(socket.gethostname())

#import socket
#import fcntl
#import struct  
def get_ip_address('eth0'):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

#def time_record()：
#	t = time.strftime('%Y%m%d%H%s',time.localtime(time.time()))
#	return t

#记录所要录入mysql的数据库的数据
Hostname = get_ip_address('eth0')
Cpu_core = getCPUstate()
Mem_total = getMemorystate().mem_total
Mem_used = getMemorystate().mem_used
Mem_free = getMemorystate().mem_free
Mem_buffer = getMemorystate().mem_buffer
Mem_cache = getMemorystate().mem_cache	
Disk_detail = disk_detail()
Os_detail = os_detail()
Outnet_ip = GetIP().outnet_IP
Innet_ip = get_ip_address('eth0')
#time_record = time_record()

# 打开数据库连接
db = MySQLdb.connect("192.168.0.173","admin","123456","monitor" )
# 使用cursor()方法获取操作游标 
cursor = db.cursor()
# SQL 插入语句
sql = "INSERT INTO MONITOR_BASIC(hostname, cpu_core, mem_total, mem_used, mem_free,mem_buffer,mem_cache,mem_swap,disk_detail,os_detal,innet_ip,outnet_ip,time) 
       VALUES ('%s','%d','%s','%s','%s','%s','%s','%s,'%s','%s','%s )" % \
       (Hostname, Cpu_core, Mem_total, Mem_used, Mem_free,Mem_buffer,Mem_cache,Disk_detail,Os_detail,Outnet_ip,Innet_ip)       
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()
# 关闭数据库连接
db.close()
