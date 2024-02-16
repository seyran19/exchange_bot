from telebot import types

markup = types.InlineKeyboardMarkup(row_width=2)
btn1 = types.InlineKeyboardButton("USD/EUR", callback_data="USD/EUR")
btn2 = types.InlineKeyboardButton("EUR/USD", callback_data="EUR/USD")
btn3 = types.InlineKeyboardButton("USD/GBP", callback_data="USD/GBP")
btn4 = types.InlineKeyboardButton("Другое значение", callback_data="else")
markup.add(btn1, btn2, btn3, btn4)
