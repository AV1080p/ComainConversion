#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import urlparse
 
def getIp(domain):
    trytime = 0
    while True:
         try:
            domain = domain.split(':')[0]
            myaddr = socket.getaddrinfo(domain,None)[0][4][0]
            return myaddr
         except:
            trytime+=1
            if trytime>3:
                return ""
 
if __name__=='__main__':
    www = "http://mottoin.com"
    hosts = urlparse.urlsplit(www)
    if ":" in hosts.netloc:
        host = hosts.netloc.split(":")[0]
        port = hosts.netloc.split(":")[1]
    else:
        host = hosts.netloc
        port = '80'
        print getIp(host)