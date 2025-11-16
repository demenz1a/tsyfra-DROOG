import telebot
from telebot import types

bot = telebot.TeleBot('8353976066:AAEvXMyk_Lz-pHiR15of0MANfTrnoXU-ClA')

@bot.message_handler(commands=['Баштоо','start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Сурамжылоону баштоо',url='https://forms.gle/RCppbSBWsTHFFtsG7'))
    markup.add(types.InlineKeyboardButton('Буттум',callback_data='ended'))
    bot.reply_to(message,'Саламатсызбы! Улантуу учун баскычты басыныз',reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'ended':
        bot.send_message(
            callback.message.chat.id,
            'Сурамжылоону бүтүргөн болсоңуз, заманбап тиркемелерди колдонуу боюнча жардам алуу үчүн биздин Telegram каналыбызга баш багыңыз @osh_project.'
        )

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Яндекс Такси колдонуу', url='https://t.me/TsyfraDroog/3'))
        markup.add(types.InlineKeyboardButton('МБанк колдонуу', url='https://t.me/TsyfraDroog/4'))
        markup.add(types.InlineKeyboardButton('Жасалма интеллект колдонуу', url='https://t.me/TsyfraDroog/5'))
        markup.add(types.InlineKeyboardButton('Түндүк кирүү', url='https://t.me/TsyfraDroog/6'))
        markup.add(types.InlineKeyboardButton('Түндүк колдонуу', url='https://t.me/TsyfraDroog/7'))

        bot.send_message(callback.message.chat.id, "Төмөнкү темалар боюнча материалдар:", reply_markup=markup)


bot.polling(none_stop=True)
