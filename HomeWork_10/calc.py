from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext
from settings import TG_TOKEN
import logging


bot = Bot(token=TG_TOKEN)

updater = Updater(token=TG_TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='HomeWork_10/bot.log')
STATES = (0, 1)

logging.info('start bot')


def start(update, context):
    name = update.effective_chat.first_name
    context.bot.send_message(update.effective_chat.id, f"<b>Привет, {name}</b>!!!\nЯ - 'Бот-калькулятор' рациональных чисел.\n"
                             "Пришли мне любой пример типа:\n<b>12 + 3*3 + 44/5</b>"
                             "\nИ я посчитаю тебе результат))", parse_mode='html')


def calc(update, context):
    example = update.message.text
    parse = example.replace(
        '*', ' * ').replace('/', ' / ').replace('+', ' + ').replace('-', ' - ').split()
    while '*' in parse or '/' in parse:
        for i in range(1, len(parse) - 1):
            if parse[i] == '*':
                oper1 = float(parse.pop(i - 1))
                oper2 = float(parse.pop(i))
                parse[i-1] = oper1 * oper2
                break
            elif parse[i] == '/':
                oper1 = float(parse.pop(i - 1))
                oper2 = float(parse.pop(i))
                parse[i-1] = oper1 / oper2
                break
    while '+' in parse or '-' in parse:
        for i in range(1, len(parse) - 1):
            if parse[i] == '+':
                oper1 = float(parse.pop(i - 1))
                oper2 = float(parse.pop(i))
                parse[i-1] = oper1 + oper2
                break
            elif parse[i] == '-':
                oper1 = float(parse.pop(i - 1))
                oper2 = float(parse.pop(i))
                parse[i-1] = oper1 - oper2
                break
    context.bot.send_message(
        update.effective_chat.id, f"Результат {''.join(str(x) for x in parse)}")
    menu(update, context)


def menu(update, context):
    context.bot.send_message(update.effective_chat.id, "Для продолжения работы кликни сюда 👉 /next\n"
                             "Для выхода клинки сюда 👉 /bye")


def next(update, context):
    context.bot.send_message(update.effective_chat.id, "Хочу еще пример:")
    calc(update, context)



def cancel(update, context):
    context.bot.send_message(update.effective_chat.id,
                             "Пока-пока! Обращайся еще)")
    return ConversationHandler.END


start_handler = CommandHandler('start', start)
calc_handler = MessageHandler(Filters.text, calc)
menu_handler = MessageHandler(Filters.text, menu)
next_handler = CommandHandler('next', next)
cancel_handler = CommandHandler('bye', cancel)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(calc_handler)
dispatcher.add_handler(menu_handler)
dispatcher.add_handler(next_handler)
dispatcher.add_handler(cancel_handler)
# conv_handler = ConversationHandler(entry_points=[start_handler],
#                                    states={STATES[0]: [calc_handler],
#                                            STATES[1]: [contin_handler]},
#                                    fallbacks=[cancel_handler])

# dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()
