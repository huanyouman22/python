#!/usr/bin/python
#coding=utf-8
DATEPV = 15233
VT = 23651
WV = 45123

#实现html格式的数据报表邮件
import smtplib
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def addimg(src,imgid):
	fp = open(src,'rb')
	msgImage = MIMEImage(fp.read())
	fp.close()
	msgImage.add_header('Content-ID',imgid)
	return msgImage

msg = MIMEMultipart('related')


def sendwaring():
        url = 'http://newapi.szprize.cn/ThrowAdvice/Index/SendThrowAdvice'
        msg = 'sb,妹子跑了，还在写代码'
        t = int(time.time())
        parms = {'open_id':'oJ34ms54MyaVKBEs5o3mCFqNwuA8','key':'sdfsdfi23eswrfj5d521dsf@@#!!%$@.1','msg':msg,'time':t}
        send_url = requests.post(url,parms)


HOST = "smtp.szprize.com"
SUBJECT = u"官网流量数据报表"
TO = "690806184@qq.com"
FROM = "denghuayi@szprize.com"
msgtext = MIMEText('''
	<table width="600" border="0" cellspacing="0" cellpadding="4">
		<tr>
			<td bgcolor="#CECFAD" height="20" style="font-size:14px">*官网性能数据 <a href="monitor.domain.com">更多</a></td>
		</tr>
		<tr>
			<td bgcolor="#EFEBDE" height="100" style="font-size:13px">
			1) 日访问量：<font color=red>DATEPV</font> 访问次数:VT 页面浏览量：45123 点击数：515122 数据流量：504MB</br>
			2) 状态码信息 <br>
			&nbsp;&nbsp;500:105 404:3264 503:214</br>
			3) 访客浏览器信息<br>
			IE:50%  firefox:10%  chrome:30%  other:10%</br>
			4) 页面信息 <br>
			&nbsp;&nbsp;/index.php 42153<br>
			&nbsp;&nbsp;/view.php 21451<br>
			&nbsp;&nbsp;/login.php 5112<br>
			</td>
		</tr>
		<tr>
			<td bgcolor="#EFEBDE" height="100" style="font-size:13px">
			==========io情况==============
			<img src="cid:io"></td>
		</tr>
		<tr>
			<td bgcolor="#EFEBDE" height="100" style="font-size:13px">
			===========CPU情况===========
			<img src="cid:cpu"></td>
		</tr><td>
		<tr>
			<td bgcolor="#EFEBDE" height="100" style="font-size:13px">
			===========内存情况==========
			<img src="cid:mem"></td>
		</tr><td>	
		<tr>
			<td bgcolor="#EFEBDE" height="100" style="font-size:13px">
			============忙碌情况=============
			<img src="cid:time"></td>
		</tr><td>
	</table>''',"html","utf-8" )
msg.attach(msgtext)
msg.attach(addimg("img/cpu_load.png","io"))
msg.attach(addimg("img/cpu.png","cpu"))
msg.attach(addimg("img/cpu_time.png","time"))
msg.attach(addimg("img/mem.png","mem"))

msg['Subject'] = SUBJECT
msg['From'] = FROM
msg['To'] = TO

try:
	server = smtplib.SMTP()
	server.connect(HOST,"25")
	server.starttls()
	server.login("denghuayi@szprize.com","p8368608")
	server.sendmail(FROM,TO,msg.as_string())
	server.quit()
	print "邮件发送成功"
except Exception,e:
	print "失败："+str(e)
