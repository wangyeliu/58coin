#!/usr/bin/env python 
# -*- coding:utf-8 -*-


from urllib import  request

#因为加盐了，所以要给他转译锅里




def agent_Test():

    url ='http://agentapi.test.58ex.com/login?userName=13822228888 & password=12345678'

    headers ={
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'http://agent.test.58ex.com',
    'Referer': 'http://agent.test.58ex.com/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko)\
      Chrome/75.0.3770.142 Safari/537.36'
    }


    req = request.Request(url,headers =headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()

    print(html)

if __name__ == '__main__':
    print(agent_Test())
