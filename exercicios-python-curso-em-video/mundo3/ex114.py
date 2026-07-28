import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('https://docs.python.org/3.14/')
except urllib.error.URLError as erro:
    print('Não foi possível acessar a página!')
else:
    print('Foi possível acessar a página!')
