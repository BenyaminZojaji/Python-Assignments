from random import *
from khayyam import JalaliDatetime
from gtts import gTTS
import pysynth as ps
import telebot
import qrcode

TOKEN = ''
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_func(message):
    bot.send_message(message.chat.id, 'Welcome ' + (message.chat.first_name) + '!')


RANDOM_NUMBER = randint(0, 99)


def new_randomNumber():
    global RANDOM_NUMBER
    RANDOM_NUMBER = randint(0, 99)


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
            if m.text == 'NEW Game':
                new_randomNumber()
                bot.send_message(m.chat.id, 'NEW Game begin. Guess new number:',
                                 reply_markup=telebot.types.ReplyKeyboardRemove(selective=True))
                bot.register_next_step_handler_by_chat_id(m.chat.id, gm1)
            elif int(m.text) < RANDOM_NUMBER:
                msg = bot.send_message(m.chat.id, 'bigger', reply_markup=markup)
                bot.register_next_step_handler(msg, gm1)
            elif int(m.text) > RANDOM_NUMBER:
                msg = bot.send_message(m.chat.id, 'lower', reply_markup=markup)
                bot.register_next_step_handler(msg, gm1)
            elif int(m.text) == RANDOM_NUMBER:
                msg = bot.send_message(m.chat.id, 'Thats right. ^^',
                                       reply_markup=telebot.types.ReplyKeyboardRemove(selective=True))
        except ValueError:
            bot.send_message(m.chat.id, 'something is wrong with your input. give me a number 😢',
                             reply_markup=telebot.types.ReplyKeyboardRemove(selective=True))
        except:
            bot.send_message(m.chat.id, 'something is wrong. Call my dad 😭\n@mrbni Error code:gm1',
                             reply_markup=telebot.types.ReplyKeyboardRemove(selective=True))
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
        if len(userBirth) == 3:
            difference = JalaliDatetime.now() - JalaliDatetime(userBirth[0], userBirth[1], userBirth[2])
            bot.send_message(m.chat.id, 'You are about ' + str(difference.days // 365))
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
            bot.send_message(m.chat.id, 'biggest number: ' + str(max(numbers)))
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
            bot.send_message(m.chat.id, 'biggest number index: ' + str(numbers.index(max(numbers))))
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


SONG = ()
NOTE = ''
STRETCH = ''


def add_note():
    global SONG
    global NOTE
    global STRETCH
    if NOTE == 'Do':
        NOTE = 'c'
    elif NOTE == 'Re':
        NOTE = 'd'
    elif NOTE == 'Mi':
        NOTE = 'e'
    elif NOTE == 'Fa':
        NOTE = 'f'
    elif NOTE == 'Sol':
        NOTE = 'g'
    elif NOTE == 'La':
        NOTE = 'a'
    else:
        NOTE = 'b'
    if STRETCH == 'Whole':
        STRETCH = 1
    elif STRETCH == 'Half':
        STRETCH = 2
    elif STRETCH == 'Quarter':
        STRETCH = 4
    elif STRETCH == 'Eighth':
        STRETCH = 8
    else:
        STRETCH = 16
    SONG += ((NOTE, STRETCH),)
    NOTE = ''
    STRETCH = ''


def set_note(name):
    global NOTE
    NOTE = name


def set_stretch(stroke):
    global STRETCH
    STRETCH = stroke


def empty_song():
    global SONG
    SONG = ()


@bot.message_handler(commands=['song'])
def song_func(m):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    btn1 = telebot.types.KeyboardButton('Lets GO!')
    markup.add(btn1)
    m = bot.send_message(m.chat.id, 'lets make a song!\npress 📤 when you are done.', reply_markup=markup)
    bot.register_next_step_handler(m, so1)


def so1(m):
    if not m.text.startswith('/'):
        if m.text != 'Lets GO!':
            set_stretch(m.text)
        if STRETCH != '' and NOTE != '':
            add_note()
        markup = telebot.types.ReplyKeyboardMarkup(row_width=4)
        btn1 = telebot.types.KeyboardButton('Do')
        btn2 = telebot.types.KeyboardButton('Re')
        btn3 = telebot.types.KeyboardButton('Mi')
        btn4 = telebot.types.KeyboardButton('Fa')
        btn5 = telebot.types.KeyboardButton('Sol')
        btn6 = telebot.types.KeyboardButton('La')
        btn7 = telebot.types.KeyboardButton('Si')
        btn8 = telebot.types.KeyboardButton('📤')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        msg = bot.send_message(m.chat.id, 'note:', reply_markup=markup)
        bot.register_next_step_handler(msg, so2)
    else:
        bot.reply_to(m, 'I expect notes not a command. 🤔',
                     reply_markup=telebot.types.ReplyKeyboardRemove(selective=True))
        bot.send_message(m.chat.id, 'now tell me your command.')


def so2(m):
    if not m.text.startswith('/'):
        if not m.text == '📤':
            set_note(m.text)
            markup = telebot.types.ReplyKeyboardMarkup(row_width=3)
            btn1 = telebot.types.KeyboardButton('Whole')
            btn2 = telebot.types.KeyboardButton('Half')
            btn3 = telebot.types.KeyboardButton('Quarter')
            btn4 = telebot.types.KeyboardButton('Eighth')
            btn5 = telebot.types.KeyboardButton('Sixteenth')
            markup.add(btn1, btn2, btn3, btn4, btn5)
            msg = bot.send_message(m.chat.id, 'stretch:', reply_markup=markup)
            bot.register_next_step_handler(msg, so1)
        else:
            try:
                if len(SONG) >= 1:
                    bot.send_message(m.chat.id, 'Here is your song:',
                                     reply_markup=telebot.types.ReplyKeyboardRemove(selective=True))
                    ps.make_wav(SONG, fn="song.wav")
                    empty_song()
                    song = open('song.wav', 'rb')
                    bot.send_voice(m.chat.id, song)
                else:
                    bot.send_message(m.chat.id, 'Just try me once!\nI won\'t let you down(just kidding, I will 😂).',
                                     reply_markup=telebot.types.ReplyKeyboardRemove(selective=True))
            except:
                bot.send_message(m.chat.id, 'something is wrong. Call my dad 😭\n@mrbni Error code:so2',
                                 reply_markup=telebot.types.ReplyKeyboardRemove(selective=True))
    else:
        bot.reply_to(m, 'I expect notes not a command. 🤔',
                     reply_markup=telebot.types.ReplyKeyboardRemove(selective=True))
        bot.send_message(m.chat.id, 'now tell me your command.')


@bot.message_handler(commands=['help'])
def help_func(message):
    bot.reply_to(message,
                 'For any issues pls contact my creator.\nbenyamin.zojaji@gmail.com\n/game -guess the number game 🎮\n/song -create your song 🎶\n/age -calculate your age 🧍\n/voice -convert text to voice 🎼\n/max -find biggest number ✔️\n/argmax -find index of biggest number ☑️\n/qrcode -make Qrcode 🧷\n/help -show commands ℹ️')


bot.polling(none_stop=True)
