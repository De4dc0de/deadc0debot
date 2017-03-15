def handle(msg, bot, reimport):
    #print("reloaded")
    #pprint(msg)
    id = msg["chat"]["id"]
    #id = msg["from"]["id"]
    if("entities" in msg and msg["entities"][0]["type"] == "bot_command"):
        #bot.sendMessage(id, "Command recognized, but not yet supported")
        if(msg["text"][0] == "/"):
            if(msg["text"] == "/help"):
                bot.sendMessage(id, """These are the commands, we actually have:
                /help to show this
                /reload to get the newest handling file
                /tutorial to learn hacking """)
            elif(msg["text"] == "/reload"):
                return reimport(id)
            elif(msg["text"] == "/tutorial"):
                bot.sendMessage(id, open("tutorial.txt").read())
            else:
                bot.sendMessage(id, "Sorry, no recognizeable command. Use /help instead")
                #bot.sendMessage(id, raw_input(msg["text"] + ": "))
            
    else:
        pass
        #Hier koennte man die Erkennung dummer Fragen einfuegen.
