import sys
import os
import re
import requests as r
import wget

class fb-dl:
    def __init__(self):
        self.fl=os.path.join('/storage/emulated/0/')
        self.el='\x1b[2K'

    def menu(self):
        print('1].High Videos Download')
        print('2].Low Videos Download')

    def choice_one(self, url):
        try:
            get=r.get(url)
            hdVideos=re.search('hd_src:"(.+?)"', get.text)[1]
        except r.ConnectionError as e:
            print('Koneksi Eror!')

        else:
            hd_url=hdVideos.replace('hd_src:"', '')
            print('\nKualitas HD: ' + hd_url)
            print('[+]Melakukan download video')
            wget.download(hd_url, self.fl)
            sys.stdout.write(self.el)
            print('\nDownload selesai!')

    def choice_two(self, url2):
        try:
            get=r.get(url2)
            sdVideos=re.search('sd_src:"(.+?)"', get.text)[1]
        except r.ConnectionError as e:
            print('Koneksi Error!')
        else:
            sd_url=sdVideos.replace('sd_src:"', '')
            print('\nKualitas SD: '+ sd_url)
            print('[+]Melakukan download video')
            wget.download(sd_url, self.fl)
            sys.stdout.write(self.el)
            print('\nDownload selesai!')

download=fb-dl()
print(download.menu())
choice=input('Pilih bro> ')
if choice=="1":
   url=str(input('Url video> '))
   print(download.choice_one(url))
if choice=="2":
   url2=str(input('Url video>. '))
   print(download.choice_two(url2))
else:
   sys.exit('Goodbye!')
