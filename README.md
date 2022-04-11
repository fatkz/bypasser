# bypasser




> 403, 401, 503... is a script written to skip the web pages you receive
> For instructions on installation, see  [Installation]. I highly recommend you follow them._
## Installation

```sh
git clone https://github.com/fatkz/bypasser.git
cd bypasser
pip3 install -r requirements.txt
```
#Usage Examples

```sh
python3 main.py  {domain} {path}
```
```

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

Domain: www.test.com                Path: admin




Test Connection:


https://www.test.com/admin [503]


Bypass Test:


https://www.test.com//admin [404]
https://www.test.com///admin [404]
https://www.test.com/admin/ [503]
https://www.test.com//admin/admin [404]
https://www.test.com/;/admin/ [404]
https://www.test.com/./admin/.. [200]
https://www.test.com/.;/admin/ [404]
https://www.test.com/.;/admin [404]
https://www.test.com/admin.json [503]


Method Test:


https://www.test.com/admin    HEAD    [503]
https://www.test.com/admin    OPTIONS    [404]
https://www.test.com/admin    GET    [503]
https://www.test.com/admin    POST    [503]
https://www.test.com/admin    PUT    [503]
https://www.test.com/admin    TRACE    [405]
https://www.test.com/admin    CONNECT    [403]
https://www.test.com/admin    PATCH    [503]


Header Test:


https://www.test.com/admin    X-Originating-IP    [503]
https://www.test.com/admin    X-Forwarded-For    [503]
https://www.test.com/admin    X-Forwarded    [503]
https://www.test.com/admin    Forwarded-For    [503]
https://www.test.com/admin    X-Remote-IP    [503]
https://www.test.com/admin    X-Remote-Addr    [503]
https://www.test.com/admin    X-ProxyUser-Ip    [503]
https://www.test.com/admin    X-Original-URL    [503]
https://www.test.com/admin    Client-IP    [503]
https://www.test.com/admin    True-Client-IP    [503]
https://www.test.com/admin    Cluster-Client-IP    [503]
https://www.test.com/admin    X-ProxyUser-Ip    [503]
https://www.test.com/admin    Host    [403]


Cross Test


https://www.test.com/admin    HEAD X-Originating-IP    [503]
https://www.test.com/admin    HEAD X-Forwarded-For    [503]
https://www.test.com/admin    HEAD X-Forwarded    [503]
https://www.test.com/admin    HEAD Forwarded-For    [503]
https://www.test.com/admin    HEAD X-Remote-IP    [503]
https://www.test.com/admin    HEAD X-Remote-Addr    [503]
https://www.test.com/admin    HEAD X-ProxyUser-Ip    [503]
https://www.test.com/admin    HEAD X-Original-URL    [503]
https://www.test.com/admin    HEAD Client-IP    [503]
https://www.test.com/admin    HEAD True-Client-IP    [503]
https://www.test.com/admin    HEAD Cluster-Client-IP    [503]
https://www.test.com/admin    HEAD X-ProxyUser-Ip    [503]
https://www.test.com/admin    HEAD Host    [403]
https://www.test.com/admin    OPTIONS X-Originating-IP    [404]
https://www.test.com/admin    OPTIONS X-Forwarded-For    [404]
https://www.test.com/admin    OPTIONS X-Forwarded    [404]
https://www.test.com/admin    OPTIONS Forwarded-For    [404]
https://www.test.com/admin    OPTIONS X-Remote-IP    [404]
https://www.test.com/admin    OPTIONS X-Remote-Addr    [404]
https://www.test.com/admin    OPTIONS X-ProxyUser-Ip    [404]
https://www.test.com/admin    OPTIONS X-Original-URL    [404]
https://www.test.com/admin    OPTIONS Client-IP    [404]
https://www.test.com/admin    OPTIONS True-Client-IP    [404]
https://www.test.com/admin    OPTIONS Cluster-Client-IP    [404]
https://www.test.com/admin    OPTIONS X-ProxyUser-Ip    [404]
https://www.test.com/admin    OPTIONS Host    [403]
https://www.test.com/admin    GET X-Originating-IP    [503]
https://www.test.com/admin    GET X-Forwarded-For    [503]
https://www.test.com/admin    GET X-Forwarded    [503]
https://www.test.com/admin    GET Forwarded-For    [503]
https://www.test.com/admin    GET X-Remote-IP    [503]
https://www.test.com/admin    GET X-Remote-Addr    [503]
https://www.test.com/admin    GET X-ProxyUser-Ip    [503]
https://www.test.com/admin    GET X-Original-URL    [503]
https://www.test.com/admin    GET Client-IP    [503]
https://www.test.com/admin    GET True-Client-IP    [503]
https://www.test.com/admin    GET Cluster-Client-IP    [503]
https://www.test.com/admin    GET X-ProxyUser-Ip    [503]
https://www.test.com/admin    GET Host    [403]
https://www.test.com/admin    POST X-Originating-IP    [503]
https://www.test.com/admin    POST X-Forwarded-For    [503]
https://www.test.com/admin    POST X-Forwarded    [503]
https://www.test.com/admin    POST Forwarded-For    [503]
https://www.test.com/admin    POST X-Remote-IP    [503]
https://www.test.com/admin    POST X-Remote-Addr    [503]
https://www.test.com/admin    POST X-ProxyUser-Ip    [503]
https://www.test.com/admin    POST X-Original-URL    [503]
https://www.test.com/admin    POST Client-IP    [503]
https://www.test.com/admin    POST True-Client-IP    [503]
https://www.test.com/admin    POST Cluster-Client-IP    [503]
https://www.test.com/admin    POST X-ProxyUser-Ip    [503]
https://www.test.com/admin    POST Host    [403]
https://www.test.com/admin    PUT X-Originating-IP    [503]
https://www.test.com/admin    PUT X-Forwarded-For    [503]
https://www.test.com/admin    PUT X-Forwarded    [503]
https://www.test.com/admin    PUT Forwarded-For    [503]
https://www.test.com/admin    PUT X-Remote-IP    [503]
https://www.test.com/admin    PUT X-Remote-Addr    [503]
https://www.test.com/admin    PUT X-ProxyUser-Ip    [503]
https://www.test.com/admin    PUT X-Original-URL    [503]
https://www.test.com/admin    PUT Client-IP    [503]
https://www.test.com/admin    PUT True-Client-IP    [503]
https://www.test.com/admin    PUT Cluster-Client-IP    [503]
https://www.test.com/admin    PUT X-ProxyUser-Ip    [503]
https://www.test.com/admin    PUT Host    [403]
https://www.test.com/admin    TRACE X-Originating-IP    [405]
https://www.test.com/admin    TRACE X-Forwarded-For    [405]
https://www.test.com/admin    TRACE X-Forwarded    [405]
https://www.test.com/admin    TRACE Forwarded-For    [405]
https://www.test.com/admin    TRACE X-Remote-IP    [405]
https://www.test.com/admin    TRACE X-Remote-Addr    [405]
https://www.test.com/admin    TRACE X-ProxyUser-Ip    [405]
https://www.test.com/admin    TRACE X-Original-URL    [405]
https://www.test.com/admin    TRACE Client-IP    [405]
https://www.test.com/admin    TRACE True-Client-IP    [405]
https://www.test.com/admin    TRACE Cluster-Client-IP    [405]
https://www.test.com/admin    TRACE X-ProxyUser-Ip    [405]
https://www.test.com/admin    TRACE Host    [405]
https://www.test.com/admin    CONNECT X-Originating-IP    [403]
https://www.test.com/admin    CONNECT X-Forwarded-For    [403]
https://www.test.com/admin    CONNECT X-Forwarded    [403]
https://www.test.com/admin    CONNECT Forwarded-For    [403]
https://www.test.com/admin    CONNECT X-Remote-IP    [403]
https://www.test.com/admin    CONNECT X-Remote-Addr    [403]
https://www.test.com/admin    CONNECT X-ProxyUser-Ip    [403]
https://www.test.com/admin    CONNECT X-Original-URL    [403]
https://www.test.com/admin    CONNECT Client-IP    [403]
https://www.test.com/admin    CONNECT True-Client-IP    [403]
https://www.test.com/admin    CONNECT Cluster-Client-IP    [403]
https://www.test.com/admin    CONNECT X-ProxyUser-Ip    [403]
https://www.test.com/admin    CONNECT Host    [403]
https://www.test.com/admin    PATCH X-Originating-IP    [503]
https://www.test.com/admin    PATCH X-Forwarded-For    [503]
https://www.test.com/admin    PATCH X-Forwarded    [503]
https://www.test.com/admin    PATCH Forwarded-For    [503]
https://www.test.com/admin    PATCH X-Remote-IP    [503]
https://www.test.com/admin    PATCH X-Remote-Addr    [503]
https://www.test.com/admin    PATCH X-ProxyUser-Ip    [503]
https://www.test.com/admin    PATCH X-Original-URL    [503]
https://www.test.com/admin    PATCH Client-IP    [503]
https://www.test.com/admin    PATCH True-Client-IP    [503]
https://www.test.com/admin    PATCH Cluster-Client-IP    [503]
https://www.test.com/admin    PATCH X-ProxyUser-Ip    [503]
https://www.test.com/admin    PATCH Host    [403]
```
