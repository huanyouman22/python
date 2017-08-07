#!/usr/bin/python
#coding=utf-8
import pexpect
import sys 
import os


servers = [
        'prize-bs1@192.168.1.7',
        'prize-bs2@192.168.1.11',
        'prize-bs3@192.168.1.3',
        'prize-bs4@192.168.1.20',
        'prize-bs5@192.168.1.22',
        'prize-bs6@192.168.1.24',
        'prize-bs7@192.168.1.26',
        'prize-bs8@192.168.1.28',
        'prize-bs9@192.168.1.30',
        'prize-bs10@192.168.1.32',
        'prize-bs11@192.168.1.37',
        'prize-bs12@192.168.1.39',
        'prize-bs13@192.168.1.41',
        'prize-bs14@192.168.1.43',
        'gerrit@192.168.1.49'];     

def sendPublicKey(servers):
        for server in servers:
                child = pexpect.spawn("ssh-copy-id -i /root/.ssh/id_rsa.pub %s" %(server))
                index = child.expect(["yes/no","password","exist",pexpect.exceptions.EOF,pexpect.TIMEOUT])
                if index != 0 and index != 1:
                        print("未向此服务器%s上传公钥" %(server))
                        child.close(force=True)
                else:
                        print("开始上传公钥")
                        child.sendline('yes')
                        child.expect("password:")
                        child.sendline('szprize2018')
                        child.expect("added")
                        print("上传完毕")
                        print
        print("全部上传完毕！")

sendPublicKey(servers)
