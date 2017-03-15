#!/usr/bin/python

import os
import configfile
import telepot
import handlefile
from pprint import pprint

bot = telepot.Bot(configfile.id)

def reimport(id):
    try:
        os.system("mv handlefile.py handlefile.py.bak; rm handlefile.pyc")
        os.system("curl https://raw.githubusercontent.com/De4dc0de/deadc0debot/master/handlefile.py --output handlefile.py")
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
        bot.sendMessage(msg["from"]["id"], "Launch failed. Loaded Backup. Kick the Bot at the next Failure")

bot.message_loop(handle)

while True:
    pass
