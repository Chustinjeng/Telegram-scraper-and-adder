#!/bin/env python3
# code by : youtube.com/theunknon

"""

you can re run setup.py 
if you have added some wrong value

"""
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"

import os, sys
import time

def banner():
	os.system('clear')
	print(f"""
	{re}╔═╗{cy}┌─┐┌┬┐┬ ┬┌─┐
	{re}╚═╗{cy}├┤  │ │ │├─┘
	{re}╚═╝{cy}└─┘ ┴ └─┘┴
	""")

def requirements():
	def csv_lib():
		banner()
		print(gr+'['+cy+'+'+gr+']'+cy+' this may take some time ...')
		os.system("""
			pip3 install cython numpy pandas
			python3 -m pip install cython numpy pandas
			""")
	banner()
	print(gr+'['+cy+'+'+gr+']'+cy+' it will take upto 10 min to install csv merge.')
	input_csv = input(gr+'['+cy+'+'+gr+']'+cy+' do you want to enable csv merge (y/n): ').lower()
	if input_csv == "y":
		csv_lib()
	else:
		pass
	print(gr+"[+] Installing requierments ...")
	os.system("""
		pip3 install telethon requests configparser
		python3 -m pip install telethon requests configparser
		touch config.data
		""")
	banner()
	print(gr+"[+] requierments Installed.\n")


def config_setup():
	import configparser
	banner()
	cpass = configparser.RawConfigParser()
	cpass.add_section('cred')
	xid = input(gr+"[+] enter api ID : "+re)
	cpass.set('cred', 'id', xid)
	xhash = input(gr+"[+] enter hash ID : "+re)
	cpass.set('cred', 'hash', xhash)
	xphone = input(gr+"[+] enter phone number : "+re)
	cpass.set('cred', 'phone', xphone)
	setup = open('config.data', 'w')
	cpass.write(setup)
	setup.close()
	print(gr+"[+] setup complete !")

def merge_csv(first, second):
	import pandas as pd
	import sys
	banner()
	file1 = pd.read_csv(first)
	file2 = pd.read_csv(second)
	print(gr+'['+cy+'+'+gr+']'+cy+' merging '+first+' & '+second+' ...')
	print(gr+'['+cy+'+'+gr+']'+cy+' big files can take some time ... ')
	merge = file1.merge(file2, on='username')
	merge.to_csv("output.csv", index=False)
	print(gr+'['+cy+'+'+gr+']'+cy+' saved file as "output.csv"\n')

def update_tool():
	import requests as r
	banner()
	source = r.get("https://raw.githubusercontent.com/th3unkn0n/TeleGram-Scraper/master/.image/.version")
	if source.text == '3':
		print(gr+'['+cy+'+'+gr+']'+cy+' alredy latest version')
	else:
		print(gr+'['+cy+'+'+gr+']'+cy+' removing old files ...')
		os.system('rm *.py');time.sleep(3)
		print(gr+'['+cy+'+'+gr+']'+cy+' getting latest files ...')
		os.system("""
			curl -s -O https://raw.githubusercontent.com/th3unkn0n/TeleGram-Scraper/master/add2group.py
			curl -s -O https://raw.githubusercontent.com/th3unkn0n/TeleGram-Scraper/master/scraper.py
			curl -s -O https://raw.githubusercontent.com/th3unkn0n/TeleGram-Scraper/master/setup.py
			curl -s -O https://raw.githubusercontent.com/th3unkn0n/TeleGram-Scraper/master/smsbot.py
			chmod 777 *.py
			""");time.sleep(3)
		print(gr+'\n['+cy+'+'+gr+']'+cy+' update compled.\n')

choices = ["install", "config", "merge", "help"]
print("What do you want to do with the setup file?")
i = 0
for choice in choices:
	print(gr+'['+cy+str(i)+gr+']'+cy+' - '+ choice)
	i += 1
action = input(gr+"Please choose a number: "+re)
action = int(action)
try:
	if action == 0: #install
		print(gr+'['+cy+'+'+gr+']'+cy+' selected module : '+re+"INSTALL")
		requirements()
	elif action == 1: #configure
		print(gr+'['+cy+'+'+gr+']'+cy+' selected module : '+re+"CONFIG")
		config_setup()
	elif action == 2: #merge
		print(gr+"Choose your two csv files that you want to merge")
		first = input(gr+"Type in your first csv file: "+re)
		second = input(gr+"Type in your second csv file: "+re)
		merge_csv(first, second)
	elif action == 3: #help
		banner()
		print("""		
	Choose 0 to install requirements
	Choose 1 to setup your config
	Choose 2 to merge 2 .csv files in one
	Choose 3 for help (which is this message)
			""")
	else:
		print('\n'+gr+'['+re+'!'+gr+']'+cy+' unknown argument : '+ str(action))
		print(gr+'['+re+'!'+gr+']'+cy+' for help use : ')
		print(gr+'$ python3 setup.py -h'+'\n')
except IndexError:
	print('\n'+gr+'['+re+'!'+gr+']'+cy+' no argument given!')
	print(gr+'['+re+'!'+gr+']'+cy+' for help use : ')
	print(gr+'['+re+'!'+gr+']'+cy+' https://github.com/th3unkn0n/TeleGram-Scraper#-how-to-install-and-use')
	print(gr+'$ python3 setup.py -h'+'\n')
