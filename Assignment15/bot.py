from random import *
from khayyam import JalaliDatetime
from gtts import gTTS
import telebot
import qrcode
TOKEN = '2039012139:AAFRlw6R9GZ7st44sQh_k-nwC47KbBcjAAA'
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start_func(message):
	bot.send_message(message.chat.id,'Welcome ' + (message.chat.first_name) + '!')
RANDOM_NUMBER = randint(0 ,99)
def new_randomNumber():
    global RANDOM_NUMBER
    RANDOM_NUMBER=randint(0 ,99)
@bot.message_handler(commands=['game'])
def game_func(m):
    msg = bot.send_message(m.chat.id, 'lets play!\nTo make it easier number is between 0-100\nGuess the number!')
    bot.register_next_step_handler(msg, gm1)
def gm1(m):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    btn1 = telebot.types.KeyboardButton('NEW Game')
    markup.add(btn1)
    if not m.text.startswith("/"):
        try:
            if m.text=='NEW Game':
                new_randomNumber()
                bot.send_message(m.chat.id, 'NEW Game begin. Guess new number:', reply_markup=telebot.types.ReplyKeyboardRemove(selective=True))
                bot.register_next_step_handler_by_chat_id(m.chat.id, gm1)
            elif int(m.text)<RANDOM_NUMBER:
                msg = bot.send_message(m.chat.id, 'bigger', reply_markup=markup)
                bot.register_next_step_handler(msg, gm1)
            elif int(m.text)>RANDOM_NUMBER:
                msg = bot.send_message(m.chat.id, 'lower', reply_markup=markup)
                bot.register_next_step_handler(msg, gm1)
            elif int(m.text)==RANDOM_NUMBER:
                msg = bot.send_message(m.chat.id, 'Thats right. ^^', reply_markup=telebot.types.ReplyKeyboardRemove(selective=True))
        except ValueError:
            bot.send_message(m.chat.id, 'something is wrong with your input. give me a number 😢', reply_markup=telebot.types.ReplyKeyboardRemove(selective=True))
        except:
            bot.send_message(m.chat.id, 'something is wrong. Call my dad 😭\n@mrbni Error code:gm1', reply_markup=telebot.types.ReplyKeyboardRemove(selective=True))
    else:
        bot.reply_to(m, 'I expect a number not a command. 🤔')
        bot.send_message(m.chat.id, 'now tell me your command.')
@bot.message_handler(commands=['age'])
def age_func(m):
    msg = bot.send_message(m.chat.id, 'Just give me your date of birth ^^ e.g. 1360/4/12')
    bot.register_next_step_handler(msg, age1)
def age1(m):
    if not m.text.startswith('/'):
        userBirth = m.text.split('/')
        if len(userBirth)==3:
            difference = JalaliDatetime.now() - JalaliDatetime(userBirth[0], userBirth[1], userBirth[2])
            bot.send_message(m.chat.id, 'You are about '+ str(difference.days//365))
        else:
            bot.reply_to(m, 'something is wrong with your input.')
    else:
        bot.reply_to(m, 'I expect your date of birth not a command. 🤔')
        bot.send_message(m.chat.id, 'now tell me your command.')
@bot.message_handler(commands=['voice'])
def voice_func(m):
    msg = bot.send_message(m.chat.id, 'Just give me your text ^^ e.g. Hey there')
    bot.register_next_step_handler(msg, vc1)
def vc1(m):
    if not m.text.startswith('/'):
        try:
            vc = gTTS(text=m.text, slow=False)
            vc.save('voice.ogg')
            voice = open('voice.ogg', 'rb')
            bot.send_voice(m.chat.id, voice)
        except:
            bot.send_message(m.chat.id, 'something is wrong. Call my dad 😭\n@mrbni Error code:vc1')
    else:
        bot.reply_to(m, 'I expect text not a command. 🤔')
        bot.send_message(m.chat.id, 'now tell me your command.')
@bot.message_handler(commands=['max'])
def max_func(m):
    msg = bot.send_message(m.chat.id, 'Just give me your numbers seprated with , ^^ e.g. 3,5,10,2,15,4')
    bot.register_next_step_handler(msg, mx1)
def mx1(m):
    if not m.text.startswith('/'):
        try:
            numbers = list(map(int, m.text.split(',')))
            bot.send_message(m.chat.id, 'biggest number: '+str(max(numbers)))
        except ValueError:
            bot.reply_to(m, 'Is that a number??😶')
        except:
            bot.send_message(m.chat.id, 'something is wrong. Call my dad 😭\n@mrbni Error code:mx1')
    else:
        bot.reply_to(m, 'I expect numbers not a command. 🤔')
        bot.send_message(m.chat.id, 'now tell me your command.')
@bot.message_handler(commands=['argmax'])
def argmax_welcome(m):
    msg = bot.send_message(m.chat.id, 'Just give me your numbers seprated with , ^^ e.g. 3,5,10,2,15,4')
    bot.register_next_step_handler(msg, agmx1)
def agmx1(m):
    if not m.text.startswith('/'):
        try:
            numbers = list(map(int, m.text.split(',')))
            bot.send_message(m.chat.id, 'biggest number index: '+str(numbers.index(max(numbers))))
        except ValueError:
            bot.reply_to(m, 'Is that a number??😶')
        except:
            bot.send_message(m.chat.id, 'something is wrong. Call my dad 😭\n@mrbni Error code:agmx1')
    else:
        bot.reply_to(m, 'I expect numbers not a command. 🤔')
        bot.send_message(m.chat.id, 'now tell me your command.')
@bot.message_handler(commands=['qrcode'])
def qrcode_func(m):
    msg = bot.send_message(m.chat.id, 'Just give me your text/url/... , ^^ e.g. https://t.me/mrbni')
    bot.register_next_step_handler(msg, qr1)
def qr1(m):
    if not m.text.startswith('/'):
        try:
            img = qrcode.make(m.text)
            img.save('QRCODE.png')
            photo = open('QRCODE.png', 'rb')
            bot.send_photo(m.chat.id, photo)
        except:
            bot.send_message(m.chat.id, 'something is wrong. Call my dad 😭\n@mrbni Error code:qr1')
    else:
        bot.reply_to(m, 'I expect numbers not a command. 🤔')
        bot.send_message(m.chat.id, 'now tell me your command.')
@bot.message_handler(commands=['help'])
def help_func(message):
	bot.reply_to(message, 'For any issues pls contact my creator.\nbenyamin.zojaji@gmail.com\n/game -guess the number game 🎮\n/age -calculate your age 🧍\n/voice -convert text to voice 🎼\n/max -find biggest number ✔️\n/argmax -find index of biggest number ☑️\n/qrcode -make Qrcode 🧷\n/help -show commands ℹ️')
bot.polling(none_stop=True)