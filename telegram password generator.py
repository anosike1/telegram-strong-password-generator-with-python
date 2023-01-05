from telegram import *
from telegram.ext import *
from random import *

API = "1982666554:AAE_SP3hvjRTVPAloOfitpExyb0tTpSbIGA"
updater = Updater (API, use_context = True)
dp = updater.dispatcher


print ('Bot has started...')

def start (update, context):
    buttons = [[KeyboardButton ("Generate Password")]]  
    context.bot.sendMessage (chat_id = update.effective_chat.id, text = f"Hello and Welcome {update.effective_chat.first_name}. Click the button below to Generate a Strong Password - 12 Characters - RIGHT NOW.", reply_markup = ReplyKeyboardMarkup(buttons))

def  messageHandler (update, context):
    if "Generate Password" in update.message.text:
        tot = []
        alph = ['a','b','c','d', 'e', 'f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E', 'F','G','H','I','J','K','L','M','N','O','P','Q','R','s','t','u','v','w','x','Y','Z']
        sym = ['/', '@', '=', '+', ',', '[',']','(', ')', '%']
        numb = ['0','1','2','3','4','5','6','7','8','9']

        for k in range (1, 5):
            x = choice (numb)
            tot.append (x)

        for k in range (1,5):
            y = choice (alph)
            tot.append (y)

        for k in range (1,5):
            z = choice (sym)
            tot.append (z)

        shuffle (tot)
        passwrd = ""
        for x in tot:
            passwrd+=x

        context.bot.send_message (chat_id = update.effective_chat.id, text = f"{passwrd}")

dp.add_handler (CommandHandler ("start", start))
dp.add_handler (MessageHandler (Filters.text, messageHandler))

updater.start_polling()
updater.idle()