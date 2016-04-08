'''
JAC:
log host and date with each cookie
finish writing get cookie()

'''
from os import listdir

def filename_encode(string):
    '''args: string\n\nreplaces non alphanumeric characters with "_" and appends ".sl"\nreturns the string'''
    return ''.join([(c if c.isalnum() else '_') for c in string])+'.sl'

def setcookie(cookie_string):
    '''args: cookie_string\n\nwrites cookie_string[:4000] to cookies.sl'''
    f = open('cookies.sl', 'a')
    f.write(cookie_string[:4000]+'\n')
    f.close()

def getcookie(url):
    return ''

def writecache(url, data):
    '''args: url, data\n\nwrites data to "cache/"+filname_encoded(url)'''
    url = filename_encode(url)
    f = open('cache/'+url, 'w')
    f.write(data)
    f.close()

def readcache(url):
    '''args: url\n\nuses os.listdir to find the filename_encoded(url) file, returns the contents'''
    filename_encode(url)
    cached = listdir('cache')
    if url in cached:
        f = open('cache/'+url, 'r')
        x = f.read()
        f.close()
        return x
