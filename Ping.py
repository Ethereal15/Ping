import os

print('Ping custom URL')

url = input('Enter URL: ')
os.system("ping %s" %url)
