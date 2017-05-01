# -*- coding: utf-8 -*-
#author:trust
import wmi
import json
import urllib2
import os
import string
import time
import sys
 
def http_get():
   try:
      url = 'http://tools.cloudxns.net/Api/getLdns'
      response = urllib2.urlopen(url)
      return response.read()
   except urllib2.URLError, e:
      pass
 
def readJson():
    dnsAdd=[]
    s=json.loads( http_get())
    status=s['status'];
    if status!='success':
        return  dnsAdd
    m_list=s['data']
    m_dict=m_list[0]
    m_list_info=m_dict['info']
    for m_dirt_vip in m_list_info:
        dnsAdd.append(m_dirt_vip['vip'])
    return dnsAdd
 
def ChooseDNS():
    DNSDIR={}
    DNSADDR=readJson()
    for dns_child in DNSADDR:
        tempStr='ping %s'%(dns_child,)
        p = os.popen(tempStr)
        strs = p.read()
        index1 = strs.rfind('ms')
        if index1==-1:
            continue
        index2 = strs.rfind('=')
        item = strs[index2 + 1:index1]
        item = item.strip()
        time = string.atoi(item)
        DNSDIR[dns_child]=time
    DNSDIR = sorted(DNSDIR.items(), key=lambda d: d[1])
    return [DNSDIR[0][0],DNSDIR[1][0]]
 
def ModifyDNS():
    wmiService = wmi.WMI()
    colNicConfigs = wmiService.Win32_NetworkAdapterConfiguration(IPEnabled=True)
    if len(colNicConfigs) < 1:
        exit()
    arrDNSServers = ChooseDNS()
    for objNicConfig in colNicConfigs:
        intReboot = 0
        returnValue = objNicConfig.SetDNSServerSearchOrder(DNSServerSearchOrder=arrDNSServers)
        if returnValue[0] == 0 or returnValue[0] == 1:
            intReboot += returnValue[0]
        else:
            returnValue = objNicConfig.SetDNSServerSearchOrder()
            # exit()
        if intReboot > 0:
            print 'need reboot'
 
if __name__ == "__main__":
    if sys.executable.endswith("pythonw.exe"):
        sys.stdout = open(os.devnull, "w");
        sys.stderr = open(os.path.join(os.getenv("TEMP"), "stderr-" + os.path.basename(sys.argv[0])), "w")
 
    while 1:
        ModifyDNS()
        time.sleep(3600)
    sys.exit()