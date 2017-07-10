def handle(msg, bot, reimport):
    import json
    import telepot
    import time
    import configfile
    import binascii
    import datetime
    import zlib
    try:
        botid = configfile.botid
    except:
        botid = "@Deadc0deBot"
    botid = botid.lower()
    #print("reloaded")
    #print(msg)
    #json.dump(msg, open("dump" + str(time.clock()) + ".txt", "w"))
    def limit(derwert, daslimit):
        if(derwert >= daslimit):
            return daslimit
        else:
            return derwert
        
    try:
        users = json.load(open("users.json"))
    except:
        users = {"nobody" : "0"}
        print("fehler 1")
    try:
        print(msg["from"]["username"] + " : " + str(msg["from"]["id"]))
        if(not msg["from"]["username"] in users):
            users[msg["from"]["username"]] = msg["from"]["id"]
    except:
        print("fehler 2 (Er hat keinen Nutzernamen)")
    try:
        json.dump(users, open("users.json", "w"))
        id = msg["chat"]["id"]
    except:
        print("fehler 3")
    #id = msg["from"]["id"]
    try:
        realtext = msg["text"]
        command = msg["text"].lower().split(" ")[0]
    except:
        pass #bot.sendMessage(id, "Sorry, i am not yet ready to interact with this")
    if("entities" in msg and "type" in msg["entities"][0] and msg["entities"][0]["type"] == "bot_command" and command[0] == "/"):
        if(True):
            if(command == "/help" or command == "/help" + botid):
                try:
                    bot.sendMessage(id, open(configfile.helpfile).read())
                except:
                    pass
            elif(command == "/reload" or command == "/reload" + botid):
                return reimport(id)
            elif(command == "/tutorial" or command == "/tutorial" + botid or command == "/needtutorial" or command == "/needtutorial" + botid):
                try:
                    bot.sendMessage(id, open(configfile.tutfile).read())
                except:
                    pass
            elif(command == "/source" or command == "/source" + botid):
                try:
                    bot.sendMessage(id, configfile.sourceurl)
                except:
                    pass
            elif(command == "/penis" or command == "/penis" + botid):
                try:
                    bot.sendMessage(id, "<" + "=" * limit(int(realtext.split(" ")[1]), 500) + "3")
                except:
                    bot.sendMessage(id, "<====3")
            elif(command == "/love" or command == "/love" + botid):
                bot.sendMessage(id, "<3")
            elif(command == "/web" or command == "/web" + botid):
                try:
                    bot.sendMessage(id, configfile.weburl)
                except:
                    pass
            elif(command == "/gidf" or command == "/gidf" + botid):
                try:
                    bot.sendMessage(id, configfile.gidfurl)
                except:
                    pass
            elif(command == "/vote" or command == "/vote" + botid):
                try:
                    votedict = json.load(open("votes.txt"))
                except:
                    votedict = {"lastvote": "nothing", "nothing": {"limit": datetime.date.today(), "votestring": "Nothing", "pro": [], "contra": []}}
                cparts = realtext.split(" ")
                try:
                    if(len(cparts) > 2):
                        if(not zlib.crc32(cparts[1]) in votedict and int(cparts[2]) > 0):
                            votedict[zlib.crc32(cparts[1])] = {"limit": datetime.date.today() + datetime.timedelta(int(cparts[2])), "votestring": cparts[1], "pro": [msg["from"]["id"]], "contra": []}
                            votedict["lastvote"] = zlib.crc32(cparts[1])
                except:
                    pass
            else:
                pass#bot.sendMessage(id, "Sorry, no recognizeable command. Use /help instead")
                #bot.sendMessage(id, raw_input(msg["text"] + ": "))
            
    else:
        try:
            if("xD" in msg["text"] or "XD" in msg["text"] or "xd" in msg["text"] or "Xd" in msg["text"]):
                bot.sendMessage(id, u'\U0001f606')
            if(msg["text"].replace(" ", "").replace("0", "").replace("1", "").replace("\n", "") == ""):
                if(len(msg["text"]) > 7 and "0" in msg["text"] or "1" in msg["text"]):
                    binaer = int("0b" + msg["text"].replace(" ", "").replace("\n", ""), 2)
                    bot.sendMessage(id, "Das ist dein Text:")
                    bot.sendMessage(id, binascii.unhexlify('%x' % binaer))
        except:
            pass
