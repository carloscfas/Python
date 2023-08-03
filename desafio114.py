import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.erro.URLError:
    print('Deu erro!')
else:
    print('Tudo Ok')
    print(site.read())
#O .read pega o conteúdo de dentro do site
