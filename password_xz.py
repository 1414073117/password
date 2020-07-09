
keydigit = ['0','1','2','3','4','5','6','7','8','9']
keybigle = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
keysmale = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
keyspeci = [' ','#','@','!','$','%','^','&','*','(',')','-','_','+','=','[',']','{','}','|','\\',';',':','\'','\"',',','<','.','>','/','?','`','~']

#递归取字典进行组合
#type为次数
def dictionary_dg(txt,type):
    if type <= 1:
        for text in txt:
            if text != "":
                yield text
    else :
        for text in txt:
            if text != "":
                for txtl in dictionary_dg(txt,type - 1):
                    if txtl != "":
                        yield text+txtl

def dictionary_dg_contain(txt,type):
    if type <= 0:
        return ""
    for i in range(1,type+1):
        for text in dictionary_dg(txt,i):
            if text != "":
                yield text.strip("\n")
#取参数文件
#url 为路径
#type = 0 获取当前文件内数量
#type = n (n>0) 获取当前文件内有序组合
def dictionary_read(url,type = 1,contain = False):
    try:
        rea = open(url,'r',encoding='utf-8')
    except Exception:
        print("无法取读当前文件")
        return ""
    if type <= 0:
        i = 0
        for text in rea:
            if text != "":
                i += 1
        yield i
    else :
        txt = rea.read().split('\n')
        if contain == False:
            for text in dictionary_dg(txt,type):
                if text != "":
                    yield text.strip("\n")
        else :
            for text in dictionary_dg_contain(txt,type):
                if text != "":
                    yield text.strip("\n")
    rea.close

#写密码文件
#url 为路径
#str 写入文件的字典
#type = n (n>0) 字典内有序组合
def dictionary_write(url,str,type = 1,contain = False):
    text = []
    for passer in dictionary_read(url,1):
        if passer != "":
            text.append(passer)
        
    rea = open(url,'a',encoding='utf-8')
    if type > 0:
        if contain == False:
            for passer in dictionary_dg(str,type):
                if passer != "" and passer not in text:
                    rea.write(passer.strip("\n")+"\n")
        else :
            for passer in dictionary_dg_contain(str,type):
                if passer != "" and passer not in text:
                    rea.write(passer.strip("\n")+"\n")
    rea.close