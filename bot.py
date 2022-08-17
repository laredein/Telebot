from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import json

token = "777777777777777777777"
bot = Updater(token, use_context = True)
bot = Updater(token, use_context = True)
arr = dict()
b = True
def text(chatid):
    global arr
    print(arr)
    s = ""
    for i in range(len(arr[str(chatid)]) - 1):
        s += "@" + arr[str(chatid)][i] + ", "
    if (len(arr[str(chatid)]) > 0):
        s += "@" + arr[str(chatid)][len(arr[str(chatid)]) - 1]
    return s
def f(update: Update, context: CallbackContext):
    global arr
    if update.message.text == 'Перекличка' or update.message.text == 'перекличка':
        chatid = update.message.chat.id
        s = text(chatid)
        s = s.split(", ")
        print(s)
        for i in range(len(s) // 4):
            p = ""
            for j in range(3):
                p += s[i * 4 + j] + ", "
            p += s[i * 4 + 3]
            update.message.reply_text(p)
            print(p)
        p=""
        for i in range(len(s) - len(s) % 4, len(s) - 1):
            p += s[i] + ", "
        if len(s) % 4 != 0:
            p += s[len(s) - 1]
        if p != "":
            update.message.reply_text(p)

    if b:
        userid = update.message.from_user
        chatid = update.message.chat.id
        if str(chatid) in arr.keys():
            if userid['username'] not in arr[str(chatid)]:
                arr[str(chatid)].append(userid['username'])
        else:
            arr[str(chatid)] = [userid['username']]
def on(update: Update, context: CallbackContext):
    global b
    b = True
    global arr
    chatid = update.message.chat.id
    with open('data.json') as js:
        newarr = json.load(js)
    if str(chatid) in newarr.keys():
        arr[str(chatid)] = newarr[str(chatid)].copy()
def off(update: Update, context: CallbackContext):
    global b
    b = False
    global arr
    with open('data.json','w') as js:
        json.dump(arr, js)
bot.dispatcher.add_handler(CommandHandler("secretfrase2", on))
bot.dispatcher.add_handler(CommandHandler("secretfrase1", off))
bot.dispatcher.add_handler(MessageHandler(Filters.all, f))

bot.start_polling()