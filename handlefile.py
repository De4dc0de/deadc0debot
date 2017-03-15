def handle(msg, bot, reimport):
    import pickle
    botid = "@Deadc0deBot"
    botid = botid.lower()
    banamount = 10
    #print("reloaded")
    #pprint(msg)
    id = msg["chat"]["id"]
    #id = msg["from"]["id"]
    if("entities" in msg and msg["entities"][0]["type"] == "bot_command"):
        #bot.sendMessage(id, "Command recognized, but not yet supported")
        realcommand = msg["text"]
        command = msg["text"].lower().split(" ")[0]
        print(command)
        if(command[0] == "/"):
            if(command == "/help"):
                bot.sendMessage(id, """These are the commands, we actually have:
                /help - show this
                /reload - get the newest handling file
                /tutorial - learn hacking
                /source - show a Link to the source of the bot
                /web - show a Link to the Web page
                /voteban @user - be evil and ban an evil user""")
            elif(command == "/reload" or command == "/reload" + botid):
                return reimport(id)
            elif(command == "/tutorial" or command == "/tutorial" + botid):
                bot.sendMessage(id, open("tutorial.txt").read())
            elif(command == "/source" or command == "/source" + botid):
                bot.sendMessage(id, "https://github.com/De4dc0de/deadc0debot")
            elif(command == "/web" or command == "/web" + botid):
                bot.sendMessage(id, "https://http://deadc0de.bplaced.net")
            elif(command == "/voteban" or command == "/voteban" + botid):
                try:
                    bandict = pickle.load(open("bandict"))
                except:
                    bandict = {}
                try:
                    banuser = realcommand.split(" ")[1]
                    if(banuser != 0):
                        if(not banuser in bandict):
                            bandict[banuser] = 1
                        else:
                            bandict[banuser] = bandict[banuser] + 1
                        lastvote = banuser
                        bot.sendMessage(id, "Voteban " + banuser + " " + str(bandict[banuser]) + "/" + str(banamount))
                except:
                    bandict[lastuser] = bandict[lastuser] + 1
                    bot.sendMessage(id, "Voteban " + lastuser + " " + str(bandict[lastuser]) + "/" + str(banamount))
                pickle.dump(bandict, open("bandict", "w"))
            else:
                bot.sendMessage(id, "Sorry, no recognizeable command. Use /help instead")
                #bot.sendMessage(id, raw_input(msg["text"] + ": "))
            
    else:
        pass
        #Hier koennte man die Erkennung dummer Fragen einfuegen.
