from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from settings import TG_TOKEN


bot = Bot(token=TG_TOKEN)

updater = Updater(token=TG_TOKEN)
dispatcher = updater.dispatcher

A = 0

def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Привет \n Я - Бот, удаляющий из текста слова, "
                             "содержащие 'абв'."
                             "\n Пришли мне любой текст и увидешь, что будет!!))")
    return A



def txt_filter(update, context):
    text = update.message.text
    if 'абв' in text.lower():
        text = list(filter(lambda x: 'абв' not in x, text.split()))
        context.bot.send_message(
            update.effective_chat.id, ' '.join(text))
    elif 'абв' not in text.lower():
        context.bot.send_message(
            update.effective_chat.id, "В твоем тексте нет слов, содержащих 'абв'")
    return ConversationHandler.END


def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, "Что то пошло не так")
    return ConversationHandler.END


start_handler = CommandHandler('start', start)
txt_filter_handler = MessageHandler(Filters.text, txt_filter)
cancel_handler = CommandHandler("cancel", cancel)

conv_handler = ConversationHandler(entry_points=[start_handler],
                                   states={A: [txt_filter_handler]},
                                   fallbacks=[cancel_handler])


dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()

