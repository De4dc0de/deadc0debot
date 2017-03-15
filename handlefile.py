def handle(msg, bot, reimport):
    import pickle
    import telepot
    botid = "@Deadc0deBot"
    botid = botid.lower()
    banamount = 10
    #print("reloaded")
    #print(msg)
    
    try:
        users = pickle.load(open("users"))
    except:
        users = {"nobody" : "0"}
    if(not msg[from][username] in users):
        users[msg[from][username]] = msg[from][id]
    pickle.dump(users, open("users", "w")
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
            elif(command == "/penis" or command == "/penis" + botid):
                bot.sendMessage(id, "<====3")
            elif(command == "/love" or command == "/love" + botid):
                bot.sendMessage(id, "<3")
            elif(command == "/web" or command == "/web" + botid):
                bot.sendMessage(id, "https://http://deadc0de.bplaced.net")
            elif(command == "/voteban" or command == "/voteban" + botid):
                try:
                    bandict = pickle.load(open("bandict"))
                except:
                    bandict = {"lastuser" : "nobody", "nobody" : 0}
                try:
                    banuser = realcommand.split(" ")[1].split("@")[1]
                    if(banuser in users):
                        #print(bot.getChat(id))
                        if(not banuser in bandict):
                            bandict[banuser] = 1
                        else:
                            bandict[banuser] = bandict[banuser] + 1
                        bandict["lastuser"] = banuser
                        bot.sendMessage(id, "Voteban " + banuser + " " + str(bandict[banuser]) + "/" + str(banamount))
                except:
                    #print(bandict["lastuser"])
                    bandict[bandict["lastuser"]] = bandict[bandict["lastuser"]] + 1
                    #print("debug2")
                    bot.sendMessage(id, "Voteban " + bandict["lastuser"] + " " + str(bandict[bandict["lastuser"]]) + "/" + str(banamount))
                    #print("debug3")
                if(bandict[bandict["lastuser"]] >= banamount):
                    kickChatMember(id, user[banuser])
                pickle.dump(bandict, open("bandict", "w"))
            else:
                bot.sendMessage(id, "Sorry, no recognizeable command. Use /help instead")
                #bot.sendMessage(id, raw_input(msg["text"] + ": "))
            
        else:
            
            if("xD" in msg["text"]):
                bot.sendMessage(id, ":funny:")
