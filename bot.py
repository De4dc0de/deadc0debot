#!/usr/bin/python

import os
import configfile
import telepot
import handlefile
from pprint import pprint

bot = telepot.Bot(configfile.id)

def reimport(id):
    try:
        os.popen("curl https://raw.githubusercontent.com/De4dc0de/deadc0debot/master/handlefile.py --output handlefile.py")
        reload(handlefile)
        print("reloaded")
        bot.sendMessage(id, "done")
    except:
        bot.sendMessage(id, "Update failed. Kick the Bot")
def handle(msg):
    try:
        handlefile.handle(msg, bot, reimport)
    except:
        bot.sendMessage(msg["from"]["id"], "Launch failed. Kick the Bot and don't write anything")

bot.message_loop(handle)

while True:
    pass
