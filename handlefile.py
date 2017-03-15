def handle(msg, bot, reimport):
    #print("reloaded")
    #pprint(msg)
    if("entities" in msg and msg["entities"][0]["type"] == "bot_command"):
        #bot.sendMessage(msg["from"]["id"], "Command recognized, but not yet supported")
        if(msg["text"] == "/reload"):
            return reimport(msg["from"]["id"])
        else:
            bot.sendMessage(msg["from"]["id"], raw_input(msg["text"] + ": "))
        #print(msg["text"])
    else:
        bot.sendMessage(msg["from"]["id"], "Sorry, no recognizeable format. Use /help instead")
        #print(msg["chat"])
