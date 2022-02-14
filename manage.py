from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from googletrans import Translator


def salom(update, context):
    context.bot.send_message(update.message.from_user.id,"Tarjima Botga xush kelibsiz!")


def tarjima(update,context):
    tr = Translator()
    leng = tr.detect(update.message.text).lang
    if leng=="en":
        context.bot.send_message(update.message.from_user.id, tr.translate(update.message.text,src="en",dest="uz").text)
    elif leng=="ru":
        context.bot.send_message(update.message.from_user.id, tr.translate(update.message.text,dest="uz",src="ru").text)
    else:
        context.bot.send_message(update.message.from_user.id, tr.translate(update.message.text).text)



def main():
    updater = Updater("5230948329:AAEsK1WESAF1CDfyEgipL7DMO4InSJUFqg4")

    dispecher = updater.dispatcher
    dispecher.add_handler(CommandHandler("start", salom))
    dispecher.add_handler(MessageHandler(Filters.text, tarjima))

    updater.start_polling()
    updater.idle


main()
