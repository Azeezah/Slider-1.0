'''
To do: make https the default protocol while still supporting sites that don't support https
use re in removeformatting to limit \n to two in a row
'''

from CacheCookies import *
from urllib.request import Request, urlopen
from socket import gethostbyname as toIP
from random import random

invalidIP = [toIP('https://www.'+str(random())[2:]+'.org') for i in range(3)]+[toIP('')]

def gethost(url):
    host = ''
    if '://' in url:
        host = url[url.index('://')+3 ::]
        if '/' in host:
            host = host[:host.index('/')]
    return host

def valid(url):
    try:
        ip = toIP(gethost(url))
        print('try block\n\thost is '+gethost(url)+'\n\turl is '+url)
    except:
        print('exception block\n\thost is '+gethost(url)+'\n\turl is '+url)
        return False
    else:
        if ip not in invalidIP:
            return True
        else:
            return False  #not necessary: returns None by default

def cleanurl(url):
    url = url.strip('/')
    if valid(url):
        return url
    prefixes = ['http://www.', 'http://']
    for prefix in prefixes:
        if valid(prefix+url):
            return prefix+url
    return False

def getorigin(url):
    return ''

def removeformatting(string, tags=['script', 'style'], encoding = {'\\n':'\n','\\r':'','\\t':'\t','&amp;':'&','&ndash;':' - ','&#36;':'$','\\xc2\\xa0':'\n*'}):
    string = string[2:-1] #removes byte conversion residue i.e. changes "b'HTML'" to "HTML"
    for tag in tags:
        start, end = '<'+tag, '</'+tag+'>'
        while start in string:
            if end in string:
                string = string[ : string.index(start)] + string[string.index(end)+len(end) : ]
            else:
                string = string[string.index(start) : ]

    #The code above removes the tags and everything in between
    #The code below just removes the tags

    out = ''
    tag = False
    for char in string:
        if char == '<':
            tag = True
        elif char == '>':
            tag = False
        elif tag == False:
            out += char

    for old, new in encoding.items():
        out = out.replace(old, new)

    return out

def GET(url, cookies_enabled = False, cache_enabled = True):
    url = cleanurl(url)
    if not url:
        return 'Error: Invalid URL'
    if cache_enabled:
        data = readcache(url)
        if data:
            print('\nGot Cache\n')
            return data
        
    headers = {
        'User-Agent' : "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 Slider/0.2.1",
#        'Host' : gethost(url),
        'Connection' : 'close',
        'Content-Length' : '0',
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Origin' : getorigin(url),
        'Cache-Control' : 'max-age=0',
        'Accept-Language' : 'en-US,en;q=0.8',
        'Cookie': getcookie(url)
    }

    req = Request(url, headers=headers)
    print('Headers: ', req.headers)
    print('URL: ', req.full_url) 
    try:
        x = urlopen(req)
    except Exception as instance:
        if instance.args:
            return "Error: "+' '.join([str(arg) for arg in instance.args])
        else:
            return "Error: Page Not Found"

    if x.code < 400 and x.code >= 200:
        if cookies_enabled and 'Set-Cookie' in x.headers.keys():
            setcookie(x.headers['Set-Cookie'])
        y = removeformatting(str(x.read()))
        if cache_enabled:
            writecache(url, y)
        return y
    return str(x.code)+' '+x.msg














'''
modeled after Chrome request:

GET /api/api_login.php HTTP/1.1
Host: pastebin.com
Connection: keep-alive
Content-Length: 162
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Origin: http://pastebin.com
User-Agent: Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36
#Content-Type: application/x-www-form-urlencoded
#Referer: http://pastebin.com/api/api_user_key.html
Accept-Encoding: gzip,deflate,sdch
Accept-Language: en-US,en;q=0.8
Cookie: __cfduid=d2b684f5c98784917903519952f13ac911454170056; PHPSESSID=u68cpgot27vlb97377c3qfqj15; pastebin_user=3f2182634f67e6f33fc0e54c86428952; _ga=GA1.2.1369987370.1454170072


headers = {
    'User-Agent' : "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 Slider/0.2.1",
#    'Host' : gethost(url),
    'Connection' : 'keep-alive',
    'Content-Length' : '0',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Origin' : getorigin(url),
    'Cache-Control' : 'max-age=0',
    'Accept-Language' : 'en-US,en;q=0.8',
    'Cookie': getcookie(url)
    }

'''