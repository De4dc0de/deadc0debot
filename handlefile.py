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
    id = msg["chat"]["id"]
    #print("reloaded")
    #print(msg)
    #json.dump(msg, open("dump" + str(time.clock()) + ".txt", "w"))
    def limit(derwert, daslimit):
        if(derwert >= daslimit):
            return daslimit
        else:
            return derwert
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
            elif(command == "/binaer" or command == "/binaer" + botid):
                try:
                    bot.sendMessage(id, ' '.join(format(ord(x), 'b').zfill(8) for x in realtext.split(" ")[1]))
                except:
                    pass
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
                    votedict = json.load(open("votes.json"))
                except:
                    votedict = {"lastvote": "nothing", "nothing": {"limit": datetime.date.today(), "votestring": "Nothing", "pro": [], "contra": []}}
                cparts = realtext.split(" ")
                try:
                    if(len(cparts) > 2):
                        if(not zlib.crc32(cparts[1].encode()) in votedict and int(cparts[2]) > 0):
                            votedict[zlib.crc32(cparts[1]).encode()] = {"limit": datetime.date.today() + datetime.timedelta(int(cparts[2])), "votestring": cparts[1], "pro": [msg["from"]["id"]], "contra": []}
                            votedict["lastvote"] = zlib.crc32(cparts[1].encode())
                            print(msg["from"]["id"] + " voted for " + cparts[1])
                    json.dump(votedict, open("votes.json", "w"))
                except:
                    pass
            else:
                pass#bot.sendMessage(id, "Sorry, no recognizeable command. Use /help instead")
                #bot.sendMessage(id, raw_input(msg["text"] + ": "))
            
    else:
        try:
            if("xD" in msg["text"] or "XD" in msg["text"] or "xd" in msg["text"] or "Xd" in msg["text"]):
                bot.sendMessage(id, u'\U0001f606')
            if("youtube." in msg["text"]):
                youtubelinks = msg["text"].split("youtube.", 1)[1:]
                hooktubelinks = []
                for i in youtubelinks:
                    hooktubelinks.append("hooktube.com/" + i.split("/", 1)[1].rsplit("/", 1)[0])
                bot.sendMessage(id, "\n".join(hooktubelinks))
            if(msg["text"].replace(" ", "").replace("0", "").replace("1", "").replace("\n", "") == ""):
                if(len(msg["text"]) > 7 and "0" in msg["text"] or "1" in msg["text"]):
                    binaer = int("0b" + msg["text"].replace(" ", "").replace("\n", ""), 2)
                    bot.sendMessage(id, "Das ist dein Text:")
                    bot.sendMessage(id, binascii.unhexlify('%x' % binaer))
        except:
            pass
