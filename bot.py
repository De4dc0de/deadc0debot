#!/usr/bin/python

import random, string, os, telepot #Usual imports

os.system("git pull") #Update everything to the newest Version. Comment out to stop updates

import configfile #Just Bot id
import handlefile #File with all the defitinitions. Normally the only file to change
from pprint import pprint

bot = telepot.Bot(configfile.id)
updates = False

def randomword(length):
    return ''.join(random.choice(string.lowercase) for i in range(length))
def reimport(id):
    updates = True #Comment this line out to stop updates
    if(updates):
        try:
            os.system("mv handlefile.py handlefile.py.bak; rm handlefile.pyc")
            os.system("curl https://raw.githubusercontent.com/De4dc0de/deadc0debot/master/handlefile.py?random=" + randomword(10) + " --output handlefile.py")
            reload(handlefile)
            print("reloaded")
            bot.sendMessage(id, "done")
        except:
            os.system("mv handlefile.py.bak handlefile.py; rm handlefile.pyc")
            reload(handlefile)
            bot.sendMessage(id, "Update failed. Loaded Backup")
def handle(msg):
    try:
        handlefile.handle(msg, bot, reimport)
    except:
        os.system("mv handlefile.py.bak handlefile.py; rm handlefile.pyc")
        reload(handlefile)
        bot.sendMessage(msg["chat"]["id"], "Launch failed. Loaded Backup. Kick the Bot at the next Failure")

bot.message_loop(handle)

while True:
    pass
