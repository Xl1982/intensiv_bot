from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# button1 = KeyboardButton('Привет')

# kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# kb.add(button1)

button1 = KeyboardButton('1')
button2 = KeyboardButton('2')
button3 = KeyboardButton('3')
button4 = KeyboardButton('4')

kb1 = ReplyKeyboardMarkup().row(button1, button2, button3, button4)


kb3 = ReplyKeyboardMarkup().row(
    button1, button2, button3
).add(KeyboardButton('Средний рад'))
button4 = KeyboardButton('4')
button5 = KeyboardButton('5')
button6 = KeyboardButton('6')
kb3.row(button4, button5)
kb3.insert(button6)


kb4 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Отправьте свой контакт', request_contact=True)
).add(
    KeyboardButton('Отправьте свою локацию', request_location=True)
)


