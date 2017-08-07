#!/usr/bin/python
#coding=utf-8
import requests
import smtplib
from email.mime.text import MIMEText  
from email.header import Header 
import simplejson
import certifi
import urllib3
import urllib3.contrib.pyopenssl
import json

urllib3.contrib.pyopenssl.inject_into_urllib3()
http = urllib3.PoolManager(
     cert_reqs='CERT_REQUIRED',
     ca_certs=certifi.where())
#邮箱设置，两种方式，一种普通方式，默认端口25，另外一种方式qq邮箱，ssl模式，端口为465
#sender = 'denghuayi@szprize.com'
#smtpserver = 'smtp.szprize.com'
#username = 'denghuayi@szprize.com'
#password = 'p8368608'
#smtp = smtplib.SMTP()
#ssl方式
sender = '690806184@qq.com'
receiver = ['p8368608@126.com','denghuayi@szprize.com','690806184@qq.com']
subject = '接口监测正常'
qqserver = 'smtp.qq.com'
ssl_peer = '465'
qq_username = '690806184@qq.com'
# 这里不是qq的登录密码，而是qq独立的一个授权码，需要通过qq邮箱页面设置而得到，
qq_pass = 'vqqamjsaqoyrbfdc'


smtp = smtplib.SMTP_SSL()
content = ''' 
服务器：http://lauchertest.szprize.cn
监控端口：xxx
运行状态：xxxx
运行时间：xxxx
'''


#监控接口返回值
payload = {'unitype':'horizontal_message','dataCode':'hm_baidu'}
r = requests.get('http://launchertest.szprize.cn/zyp/api/datas',params=payload)
c = r.json()
msg = MIMEText(content+str(r.json()),'text','utf-8')
msg['From'] = sender
msg['To'] = ";".join(receiver)
msg['Subject'] = Header(subject,'utf-8')
result = r.json()[u'code']
user = 'denghuayi'
subject = '端口检测'


def Getoken():
	url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
	pid = {'corpid':'wx13a050fc7fd8c376', 'corpsecret':'vU7np9jZ-luplM1Bho1YE7wjt2ceOAJTUgyhc3izeX5WAClCsRV6bGGTSeu1cJwe'}
	r_json = requests.post(url,params=pid,)
	r_token = json.loads(r_json.text)["access_token"]
	return r_token

def senddata():
	url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token='+Getoken()
	message = {
   "touser": "denghayi",
   "toparty": '2',
   "totag": '3',
   "msgtype": "text",
   "agentid": '1',
   "text": content,
   "safe":0 ,
	}
	send_url = requests.post(url,message)


if result == "00000":   
        smtp.connect(qqserver,ssl_peer)
        smtp.login(qq_username,qq_pass)
        smtp.sendmail(sender,receiver,msg.as_string())
        smtp.close()
        senddata()

