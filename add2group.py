#!/bin/env python3
from cgitb import small
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, UserIdInvalidError
from telethon.tl.functions.channels import InviteToChannelRequest
import configparser
import os, sys
import csv
import traceback
import time
import random
import glob

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"

#function to edit the original member file and export the remaining list of member into a new CSV file
#done so by reading the old csv file and writing new csv file that consists of only those who are not added
def save_and_exit(input_file, n, name):
    with open(input_file) as f:
        csv_reader = csv.reader(f)
        with open("%s.csv" %(name), "w", newline = '') as new_file:
            csv_writer = csv.writer(new_file, delimiter=",", lineterminator="\n")
            i = 0
            for row in csv_reader:
                if i > n or i == 0:
                    csv_writer.writerow(row)
                i += 1


def banner():
    print(f"""
{re}╔╦╗{cy}┌─┐┬  ┌─┐{re}╔═╗  ╔═╗{cy}┌─┐┬─┐┌─┐┌─┐┌─┐┬─┐
{re} ║ {cy}├┤ │  ├┤ {re}║ ╦  ╚═╗{cy}│  ├┬┘├─┤├─┘├┤ ├┬┘
{re} ╩ {cy}└─┘┴─┘└─┘{re}╚═╝  ╚═╝{cy}└─┘┴└─┴ ┴┴  └─┘┴└─

            version : 1.0
        """)

cpass = configparser.RawConfigParser()
cpass.read('config.data')

try:
    api_id = cpass['cred']['id']
    api_hash = cpass['cred']['hash']
    phone = cpass['cred']['phone']
    client = TelegramClient(phone, api_id, api_hash)
except KeyError:
    os.system('clear')
    banner()
    print(re+"[!] run python3 setup.py first !!\n")
    sys.exit(1)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    os.system('clear')
    banner()
    client.sign_in(phone, input(gr+'[+] Enter the code: '+re))

#allows user to choose the csv file they reference to add to new group
path = os.getcwd()
extension = 'csv'
os.chdir(path)
result = glob.glob('*.{}'.format(extension)) #lists out all of the csv files in current directory
print(result) #prints out csv files
csv_file = input(gr+"Please type down the csv file you want to pass in the function: "+re)
 
os.system('clear')
banner()
input_file = csv_file
users = []
try:
    with open(input_file, encoding='UTF-8') as f:
        rows = csv.reader(f,delimiter=",",lineterminator="\n")
        next(rows, None)
        for row in rows:
            user = {}
            user['username'] = row[0]
            user['id'] = int(row[1])
            user['access_hash'] = int(row[2])
            user['name'] = row[3]
            users.append(user)
except FileNotFoundError:
    print(re+"YO type in the csv file name properly BRO")
    sys.exit(1)

 
chats = []
last_date = None
chunk_size = 200
groups=[]
 
result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
chats.extend(result.chats)
 
for chat in chats:
    groups.append(chat)
 
i=0
for group in groups:
    print(gr+'['+cy+str(i)+gr+']'+cy+' - '+group.title)
    i+=1

print(gr+'[+] Choose a group to add members')
g_index = input(gr+"[+] Enter a Number : "+re)
target_group=groups[int(g_index)]
 
#target_group_entity = InputPeerChannel(target_group.id,target_group.access_hash) 
n = 0
errorNum = 0
addedNum = 0

#name new csv file to include members who are not added in the new group
name = input(gr+"[+] Please name your new csv file: "+re)
os.system('clear')

#program to decide how long to keep the script running
seconds = 1
minutes = 60
hours = 3600
interval = 0
print(gr+"[+] Choose how long you want the program to run for"+re)
how_long = input(gr+"[+] Please enter a value for how long the program should run: "+re)
how_long = int(how_long)
print(gr+" [+] Please choose your time interval")
times = ["seconds", "minutes", "hours"]
j = 0
for t in times:
    print(gr+'['+str(j)+'] '+t)
    j += 1
ans_1 = input(gr+"Please enter a number: "+re)
ans_1 = int(ans_1)
if not (ans_1 >= 0 and ans_1 < len(times)):
    raise Exception("yo please pick a correct number bro")
if ans_1 == 0:
    interval = seconds
elif ans_1 == 1:
    interval = minutes
elif ans_1 == 2:
    interval = hours
how_long = how_long * interval
print(gr+"Program will run for %d seconds!" %(how_long))
os.system('clear')

#program to select intervals
total_time = 0
time1 = input(gr+"[+] Please enter a value for the interval: "+re)
time1 = int(time1)
print(gr+" [+] Please select a time interval: "+re)
j = 0
for t in times:
    print(gr+'['+str(j)+'] '+t)
    j += 1
ans = input(gr+"[+] Please select a number: "+re)
ans = int(ans)
if ans == 0:
    interv = seconds
elif ans == 1:
    interv = minutes
elif ans == 2:
    interv = hours
else:
    raise Exception("yo pls pick a correct number bro")
total_time = time1 * interv
os.system('clear')
print(gr+"The program will add users at intervals of %d seconds!" %(total_time))

time_start = time.time()
timeout = how_long
#program starts to add users here
for user in users:
    n += 1 #increments the number of users by 1
    if n % 50 == 0:
        print("taking a break after %d users" %(n))
        time.sleep(5) #for every multiple of 50, sleep 5 seconds
    try:
        print(gr+ "Adding {}".format(user['id']))
        time_now = time.time()
        if time_now + total_time >= time_start + timeout: #check if the time will exceed the time limit
            print(re+"time limit exceeded!") #if exceed then the program will break the loop
            n -= 1
            break
        print(gr+"Waiting for %d seconds, pls be patient" %(total_time))
        time.sleep(total_time) #the time for the script to rest before adding the next person
        user_to_add = InputPeerUser(user['id'], user['access_hash'])
        client(InviteToChannelRequest(target_group.id, [user_to_add]))
        addedNum += 1
        print(gr+"added successfully!")
    except PeerFloodError:
        print(re+"[!] Getting Flood Error from tele! \n[!] Script is stopping now. \n[i] Please try again later after some time!")
        save_and_exit(input_file, n, name)
        sys.exit(1)
    except UserPrivacyRestrictedError:
        print(re+"[i] The user's privacy setting does not allow you to do this. Skipping...")
        errorNum += 1
    except UserIdInvalidError:
        print(re+"[i] Invalid user id!")
        errorNum += 1
        continue
    except:
        traceback.print_exc()
        print(re+"[!] Unexpected Error")
        errorNum += 1
        continue

save_and_exit(input_file, n, name)

os.remove(input_file)
print("Total number of members passed in is %d" %(n))
print("Total added is %d" %(addedNum))
print("Num of skipped people is %d" %(errorNum))
