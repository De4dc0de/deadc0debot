#!/usr/bin/python

import configfile
import telepot
import handlefile
from pprint import pprint

bot = telepot.Bot(configfile.id)

def reimport(id):
    reload(handlefile)
    print("reloaded")
    bot.sendMessage(id, "done")
def handle(msg):
    handlefile.handle(msg, bot, reimport)

bot.message_loop(handle)

while True:
    pass
