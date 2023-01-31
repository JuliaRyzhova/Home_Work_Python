from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from random import randint
from settings import TG_TOKEN


bot = Bot(token=TG_TOKEN)

updater = Updater(token=TG_TOKEN)
dispatcher = updater.dispatcher
STATES = (0,1,2)

total_sweet = 120
take_sweet = 0
human_sweet = 0
bot_sweet = 0
max_take = 28
min_take = 1


def start_game(update, context):
    context.bot.send_message(
        update.effective_chat.id, "Поиграй со мной!!!\n"
        "На столе лежит 120 конфет. Ты играешь против Бота делая ход друг после друга.\n"
        "Первый ход определяется жеребьевкой. За один ход можно забрать не более чем 28 конфет.\n"
        "Победитель - тот, кто оставил на столе 0 конфет!!\n"
        "Для жеребьевки кликни сюда -> /draw")
    return STATES[0]


def first_step(update, context):
    rnd = randint(1, 2)
    if rnd == 1:
        context.bot.send_message(
            update.effective_chat.id, "Ты ходишь первый. Поехали!")
        human_step(update, context)
        return STATES[2]
    else:
        context.bot.send_message(
            update.effective_chat.id, "Бот ходит первый")
        bot_step(update, context)
        return STATES[1]


def human_step(update, context):
    global total_sweet
    global take_sweet
    global human_sweet
    context.bot.send_message(
        update.effective_chat.id, f'Ваш ход. Сейчас на столе {total_sweet} конфет(ы).\n'
        'Сколько берете конфет?')
    take_sweet = int(update.message.text)
    while take_sweet > max_take or take_sweet < min_take or take_sweet > total_sweet:
        context.bot.send_message(
            update.effective_chat.id, 'Неверное количество конфет. Попробуйте снова: ')
        take_sweet = int(update.message.text)
    total_sweet -= take_sweet
    human_sweet += take_sweet
    if total_sweet > 0:
        bot_step(update, context)
        return STATES[1]
    else:
        context.bot.send_message(
            update.effective_chat.id, 'Ты победил!!!!!!')
        return ConversationHandler.END


def bot_step(update, context):
    global total_sweet
    global take_sweet
    global bot_sweet
    if total_sweet % (min_take + max_take) != 0:
        take_sweet = total_sweet % (min_take + max_take)
    else:
        take_sweet = randint(min_take, max_take)
    context.bot.send_message(
        update.effective_chat.id, f'Бот взял {take_sweet} конфет(ы)')
    total_sweet -= take_sweet
    bot_sweet += take_sweet
    if total_sweet > 0:
        human_step(update, context)
        return STATES[2]
    else:
        context.bot.send_message(
            update.effective_chat.id, 'Бот выйграл!!!!!!!')
        return ConversationHandler.END


def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, "Что то пошло не так")


start_game_handler = CommandHandler('start', start_game)
first_step_handler = CommandHandler('draw', first_step)
human_step_handler = MessageHandler(Filters.text, human_step)
bot_step_handler = MessageHandler(None, bot_step)
cancel_handler = CommandHandler('cancel', cancel)

conv_handler = ConversationHandler(entry_points=[start_game_handler],
                                   states={STATES[0]: [first_step_handler],
                                           STATES[1]: [bot_step_handler],
                                           STATES[2]: [human_step_handler]},
                                   fallbacks=[cancel_handler])

dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()
