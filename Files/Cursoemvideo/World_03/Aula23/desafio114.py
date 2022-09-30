
import urllib.request

try:
    site = urllib.request.urlopen('http://www.facebook.com')
except:
    print('Deu erro! Site não acessível!')
else:
    print('Tudo ok')
    print(site.read())