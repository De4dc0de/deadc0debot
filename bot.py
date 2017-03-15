#!/usr/bin/python

import os
import configfile
import telepot
import handlefile
from pprint import pprint

bot = telepot.Bot(configfile.id)

def reimport(id):
    os.system("wget https://raw.githubusercontent.com/De4dc0de/deadc0debot/master/handlefile.py -O handlefile.py")
    reload(handlefile)
    print("reloaded")
    bot.sendMessage(id, "done")
def handle(msg):
    handlefile.handle(msg, bot, reimport)

bot.message_loop(handle)

while True:
    pass
