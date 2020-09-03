import sys
import os
import re
import requests as r
import wget
from colorama import Fore, init, Style, Back
init(autoreset=True)
class fb_dl:
    def __init__(self):
        self.el='\x1b[2K'

    def menu(self):
        print(Fore.GREEN + Style.BRIGHT + '''
		      ╭━┳━╭━╭━╮╮
		      ┃   ┣▅╋▅┫┃
		      ┃ ╰━╰━━━━━━╮
		      ╰┳╯       ◢▉◣
 		       ┃        ▉▉▉
		       ┃        ◥▉◤
		       ┃  ╭━┳━━━━╯
		       ┣━━━━━━┫
		      ╭╯　  　╰╮

	       ╔══════════════════════════╗''' + Back.RED +'''
\t\tFacebook videos downloader''' + Fore.GREEN + Style.BRIGHT)
        print(Fore.GREEN + Style.BRIGHT + '	       ╚══════════════════════════╝\n')
        print(Style.BRIGHT+'[1]High Videos Download')
        print(Style.BRIGHT+'[2]Low Videos Download')

    def choice_one(self, url):
        try:
            get=r.get(url)
            hdVideos=re.search('hd_src:"(.+?)"', get.text)[1]
        except r.ConnectionError as e:
            print('Koneksi Eror!')
        except TypeError:
            sys.exit('Video bersifat privat!\nTidak bisa di download!')

        else:
            hd_url=hdVideos.replace('hd_src:"', '')
            print(Style.BRIGHT+'[+]Melakukan download video')
            wget.download(hd_url)
            sys.stdout.write(self.el)

    def choice_two(self, url2):
        try:
            get=r.get(url2)
            sdVideos=re.search('sd_src:"(.+?)"', get.text)[1]
        except r.ConnectionError as e:
            print('Koneksi Error!')
        except TypeError:
            sys.exit('Video bersifat privat!\nTidak bisa di download!')
        else:
            sd_url=sdVideos.replace('sd_src:"', '')
            print(Style.BRIGHT+'[+]Melakukan download video')
            wget.download(sd_url)
            sys.stdout.write(self.el)

download=fb_dl()
os.system('clear')
download.menu()
choice=input(Style.BRIGHT+'[?]Pilih bossque? ')
if choice=="1":
      print(Fore.GREEN+Style.BRIGHT+Back.RED+'\n\tProses Download HD Quality!')
      url=str(input(Style.BRIGHT+'\n[?]Url video? '))
      download.choice_one(url)
      print(Fore.GREEN+Style.BRIGHT+Back.RED+'\nDownload Berhasil')
if choice=="2":
      print(Fore.GREEN+Style.BRIGHT+Back.RED+'\n\tProses Download SD Quality!')
      url2=str(input('\n[?]Url video? '))
      download.choice_two(url2)
      print(Fore.GREEN+Style.BRIGHT+Back.RED+'\nDownload Berhasil')
else:
      sys.exit('Goodbye!')
