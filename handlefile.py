def handle(msg, bot, reimport):
    #print("reloaded")
    #pprint(msg)
    id = msg["chat"]["id"]
    #id = msg["from"]["id"]
    if("entities" in msg and msg["entities"][0]["type"] == "bot_command"):
        #bot.sendMessage(id, "Command recognized, but not yet supported")
        command = msg["text"].lower()
        if(command[0] == "/"):
            if(command == "/help"):
                bot.sendMessage(id, """These are the commands, we actually have:
                /help to show this
                /reload to get the newest handling file
                /tutorial to learn hacking""")
            elif(command == "/reload"):
                return reimport(id)
            elif(command == "/tutorial"):
                bot.sendMessage(id, open("tutorial.txt").read())
            elif(command == "/source"):
                bot.sendMessage(id, "https://github.com/De4dc0de/deadc0debot")
            else:
                bot.sendMessage(id, "Sorry, no recognizeable command. Use /help instead")
                #bot.sendMessage(id, raw_input(msg["text"] + ": "))
            
    else:
        pass
        #Hier koennte man die Erkennung dummer Fragen einfuegen.
