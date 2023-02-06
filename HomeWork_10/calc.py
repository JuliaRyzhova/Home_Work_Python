from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext
from settings import TG_TOKEN
from logger import logger_start, logger_input_data, logger_result, logger_menu, logger_next, logger_exit


bot = Bot(token=TG_TOKEN)

updater = Updater(token=TG_TOKEN)
dispatcher = updater.dispatcher


STATES = (0, 1)


def start(update, context):
    name = update.effective_chat.first_name
    context.bot.send_message(update.effective_chat.id, f"<b>Привет, {name}</b>!!!\nЯ - 'Бот-калькулятор' рациональных чисел.\n"
                             "Пришли мне любой пример типа:\n<b>12 + 3*3 + 44/5</b>"
                             "\nИ я посчитаю тебе результат))", parse_mode='html')
    logger_start(update)


def calc(update, context):
    example = update.message.text
    logger_input_data(update, example)
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
    result = ''.join(str(x) for x in parse)
    context.bot.send_message(
        update.effective_chat.id, f"Результат {result}")
    logger_result(update, result)
    menu(update, context)


def menu(update, context):
    context.bot.send_message(update.effective_chat.id, "Для продолжения работы кликни сюда 👉 /next\n"
                             "Для выхода клинки сюда 👉 /bye")
    logger_menu(update)


def next(update, context):
    context.bot.send_message(update.effective_chat.id, "Хочу еще пример:")
    logger_next(update)


def cancel(update, context):
    context.bot.send_message(update.effective_chat.id,
                             "Пока-пока! Обращайся еще)")
    logger_exit(update)
    return ConversationHandler.END


start_handler = CommandHandler('start', start)
next_handler = CommandHandler('next', next)
cancel_handler = CommandHandler('bye', cancel)
calc_handler = MessageHandler(Filters.text, calc)
menu_handler = MessageHandler(Filters.text, menu)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(next_handler)
dispatcher.add_handler(cancel_handler)
dispatcher.add_handler(calc_handler)
dispatcher.add_handler(menu_handler)


updater.start_polling()
updater.idle()
