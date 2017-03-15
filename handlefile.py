def handle(msg, bot, reimport):
    #print("reloaded")
    #pprint(msg)
    if("entities" in msg and msg["entities"][0]["type"] == "bot_command"):
        #bot.sendMessage(msg["from"]["id"], "Command recognized, but not yet supported")
        if(msg["text"][0] == "/"):
            if(msg["text"] == "/reload"):
                return reimport(msg["from"]["id"])
            elif(msg["text"] == "/tutorial"):
                bot.sendMessage(msg["from"]["id"], open("tutorial.txt").read())
            else:
                bot.sendMessage(msg["from"]["id"], "Sorry, no recognizeable command. Use /help instead")
                #bot.sendMessage(msg["from"]["id"], raw_input(msg["text"] + ": "))
            #print(msg["text"])
    else:
        pass
        #Hier koennte man die Erkennung dummer Fragen einfuegen
