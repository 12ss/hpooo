import os
import requests
import telebot
import random,string
from telebot import types
from user_agent import generate_user_agent
import re
from secrets import choice

tok='2067895209:AAFZP5ieGCJ_Do3fO4wGmjWP0CxkhwZWBUM'
bot=telebot.TeleBot(tok)

@bot.message_handler(commands=['start'])
def send_msg(message):
    key=types.InlineKeyboardMarkup(row_width=3)
    st=types.InlineKeyboardButton("اضغط هنا",callback_data='start')
    key.add(st)
    bot.send_message(message.chat.id,"مرحبا بك في بوت حبو وحبوبو 😍",reply_markup=key)
@bot.callback_query_handler(func=lambda call: True)
def make(call):
    if call.data == 'start':
        key = types.InlineKeyboardMarkup(row_width=3)
        st1 = types.InlineKeyboardButton("تاريخ تعارفنه 😍", callback_data='dayone')
        st2 = types.InlineKeyboardButton("تاريخ اول لقاء 🤤", callback_data='visat')
        key.add(st2,st1)
        bot.edit_message_text(chat_id=(call.message.chat.id),message_id=(call.message.id),text="█▓▒▒░░░ اخــــــتـار ░░░▒▒▓█",reply_markup=key)
    if call.data == 'dayone':
        key = types.InlineKeyboardMarkup(row_width=3)
        st3 = types.InlineKeyboardButton("رجوع", callback_data='back')
        key.add(st3)
        bot.edit_message_text(chat_id=(call.message.chat.id), message_id=(call.message.id), text="يوم الجمعة : 𝟐𝟎𝟏𝟔/𝟏𝟏/𝟏𝟏 ",reply_markup=key)
    if call.data == 'visat':
        key = types.InlineKeyboardMarkup(row_width=3)
        st3 = types.InlineKeyboardButton("رجوع", callback_data='back')
        key.add(st3)
        keyboard = types.InlineKeyboardMarkup()
        bot.edit_message_text(chat_id=(call.message.chat.id), message_id=(call.message.id),text="يوم الاربعاء : 𝟐𝟎𝟐𝟏/𝟏𝟎/𝟐𝟎", reply_markup=key)
    if call.data == 'back':
        key = types.InlineKeyboardMarkup(row_width=3)
        st1 = types.InlineKeyboardButton("تاريخ تعارفنه 😍", callback_data='dayone')
        st2 = types.InlineKeyboardButton("تاريخ اول لقاء 🤤", callback_data='visat')
        key.add(st2, st1)
        bot.edit_message_text(chat_id=(call.message.chat.id), message_id=(call.message.id), text="█▓▒▒░░░ اخــــــتـار ░░░▒▒▓█",
                              reply_markup=key)

bot.polling()


