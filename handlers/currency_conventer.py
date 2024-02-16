from currency_exchange.currency import Currency
from telebot.types import Message, CallbackQuery
from loader import bot
from keyboards import markup

currency = Currency()
amount = 0


@bot.message_handler(commands=["currency"])
def bot_start(message: Message):
    bot.reply_to(message,
                 f"Введите суммму!")
    bot.register_next_step_handler(message, summa)


def summa(message: Message):
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, "Неверный формат, впишите сумму")
        bot.register_next_step_handler(message, summa)
        return
    if amount > 0:
        bot.send_message(message.chat.id, "Выберите пару валют", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Число должно быть больше чем 0, впишите сумму")
        bot.register_next_step_handler(message, summa)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call: CallbackQuery):
    if call.data != "else":
        values = call.data.split("/")
        res = currency.do_request(values[0], values[1], amount)
        bot.send_message(call.message.chat.id, f"Получается: {res} {values[1]}.\nМожете снова вписать сумму!")
        bot.register_next_step_handler(call.message, summa)
    else:
        bot.send_message(call.message.chat.id, "Введите пару значений через слэш.")
        bot.register_next_step_handler(call.message, my_currency)


def my_currency(message: Message):
    values = message.text.upper().split("/")
    res = currency.do_request(values[0], values[1], amount)
    if res is not None:
        bot.send_message(message.chat.id, f"Получается: {res} {values[1]}.\nМожете снова вписать сумму!")
        bot.register_next_step_handler(message, summa)
    else:
        bot.send_message(message.chat.id, "Что-то не так. Впишите значение заново.")
        bot.register_next_step_handler(message, my_currency)
