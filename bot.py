#!/usr/bin/python

import random, string, os, telepot #Usual imports

try:
    import configfile #Just some config
except:
    os.system("cp configfile.py.sample configfile.py")
    try:
        os.system("nano configfile.py")
    except:
        os.system("vi configfile.py")
    import configfile #And again

try:
    os.chdir(os.path.dirname(os.path.realpath(__file__))) #Change to this directory
except:
    print("Could not change directory")
    
if(configfile.updates): #Change this in config
    os.system("git pull") #Update everything to the newest Version.

import handlefile #File with all the defitinitions. Normally the only file to change except the config file
from pprint import pprint

bot = telepot.Bot(configfile.id) #Need to define this here, because other functions need this
    
def randomword(length): #Just returns a random string. Needed for uncached download
    return ''.join(random.choice(string.lowercase) for i in range(length))

def reimport(id): #Reload the definitins file. Disable this in config.py
    if(configfile.updates):
        try:
            os.system("mv handlefile.py handlefile.py.bak; rm handlefile.pyc")
            if(configfile.beta):
                os.system("curl https://raw.githubusercontent.com/De4dc0de/deadc0debot/master/handlefileedit.py?random=" + randomword(10) + " --output handlefile.py")
            else:
                os.system("curl https://raw.githubusercontent.com/De4dc0de/deadc0debot/master/handlefile.py?random=" + randomword(10) + " --output handlefile.py")
            reload(handlefile)
            print("reloaded")
            bot.sendMessage(id, "done")
        except:
            os.system("mv handlefile.py.bak handlefile.py; rm handlefile.pyc")
            reload(handlefile)
            bot.sendMessage(id, "Update failed. Loaded Backup")
def handle(msg): #Wrapper for the outsourced and more advanced handle function
    try:
        handlefile.handle(msg, bot, reimport)
    except:
        os.system("mv handlefile.py.bak handlefile.py; rm handlefile.pyc")
        reload(handlefile)
        bot.sendMessage(msg["chat"]["id"], "Launch failed. Loaded Backup. Kick the Bot at the next Failure")

bot.message_loop(handle)

while True:
    pass
